from flask import * 
from database import*
import uuid



school=Blueprint('school',__name__)

@school.route('/school_home')
def school_home():

	return render_template('school_home.html')


@school.route('/school_managestudent',methods=['post','get'])
def school_managestudent():
	data={}
	cid=session['login_id']
	q="select * from student  where study_id='%s'"%(cid)
	res=select(q)
	data['stafffview']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='delete':
		q="delete from student where student_id='%s'"%(cid)
		delete(q)
		return redirect(url_for('school.school_managestudent'))


	if action=='update':
		q="select * from student where student_id='%s'"%(cid)
		res=select(q)
		data['stafff']=res

	if "update" in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		
		q="update student set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where student_id='%s'"%(fname,lname,place,num,email,cid)
		update(q)
		return redirect(url_for('school.school_managestudent'))
		

	if "stafff" in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="insert into login values (null,'%s','%s','student')"%(uname,pwd)
		id=insert(q)
		
		q="insert into student values(null,'%s','%s','%s','%s','%s','%s','%s','school')"%(id,fname,lname,place,num,email,cid)

		insert(q)
		return redirect(url_for('school.school_managestudent'))

	return render_template('school_managestudent.html',data=data)


@school.route('/school_viewscho')
def school_viewscho():
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

		
		return redirect(url_for('school.school_viewscho'))


	if action=='update':
		q="update scholarship set status='accept' where scholarship_id='%s'"%(cid)
		update(q)
		
		return redirect(url_for('school.school_viewscho'))


	return render_template('school_viewscho.html',data=data)

@school.route('/school_viewrequest')
def school_viewrequest():
	data={}
	cid=request.args['cid']
	q="select * from request inner join student using (student_id) where scholarship_id='%s'"%(cid)
	res=select(q)
	data['seee']=res
	return render_template('school_viewrequest.html',data=data)