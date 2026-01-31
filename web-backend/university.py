from flask import * 
from database import*



university=Blueprint('university',__name__)

@university.route('/universityhome')
def universityhome():

	return render_template('universityhome.html')


@university.route('/university_addcollege',methods=['post','get'])
def university_addcollege():
	data={}
	
	q="select * from college  "
	res=select(q)
	data['stafffview']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='delete':
		q="delete from college where college_id='%s'"%(cid)
		delete(q)
		return redirect(url_for('university.university_addcollege'))


	if action=='update':
		q="select * from college where college_id='%s'"%(cid)
		res=select(q)
		data['stafff']=res

	if "update" in request.form:
		fname=request.form['fname']
		
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		
		q="update college set fname='%s',place='%s',phone='%s',email='%s' where college_id='%s'"%(fname,place,num,email,cid)
		update(q)
		return redirect(url_for('university.university_addcollege'))
		

	if "stafff" in request.form:
		fname=request.form['fname']
		
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="insert into login values (null,'%s','%s','college')"%(uname,pwd)
		id=insert(q)
		
		q="insert into college values(null,'%s','%s','%s','%s','%s')"%(id,fname,place,num,email)

		insert(q)
		return redirect(url_for('university.university_addcollege'))

	return render_template('university_addcollege.html',data=data)



@university.route('/university_viewscho')
def university_viewscho():
	data={}
	q="select * from scholarship  "
	res=select(q)
	data['annnoo']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
		
	else:
		action=None

	if action=='accept':
		q="update scholarship set status='accept' where scholarship_id='%s'"%(cid)
		update(q)

		
		return redirect(url_for('university.university_viewscho'))


	if action=='update':
		q="update scholarship set status='accept' where scholarship_id='%s'"%(cid)
		update(q)
		
		return redirect(url_for('university.university_viewscho'))


	return render_template('university_viewscho.html',data=data)

@university.route('/university_viewrequest')
def university_viewrequest():
	data={}
	cid=request.args['cid']
	q="select * from request inner join student using (student_id) where scholarship_id='%s'"%(cid)
	res=select(q)
	data['seee']=res
	return render_template('university_viewrequest.html',data=data)





@university.route('/university_viewadmission')
def university_viewadmission():
	data={}
	cid=request.args['cid']
	q="select * from admission inner join course using (course_id) inner join student using (student_id) where course_id='%s'"%(cid)
	res=select(q)
	data['seee']=res
	return render_template('university_viewadmission.html',data=data)

@university.route('/university_viewuploadeddetails')
def university_viewuploadeddetails():
	data={}
	adid=request.args['adid']
	q="select * from uploaddetails inner join admission using (admission_id) where admission_id='%s'"%(adid)
	res=select(q)
	data['seee']=res
	return render_template('university_viewuploadeddetails.html',data=data)

