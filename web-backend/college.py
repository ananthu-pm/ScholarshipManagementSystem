from flask import * 
from database import*
import uuid



college=Blueprint('college',__name__)

@college.route('/college_home')
def college_home():

	return render_template('college_home.html')



@college.route('/college_managestaff',methods=['post','get'])
def college_managestaff():
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
		return redirect(url_for('college.college_managestaff'))


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
		return redirect(url_for('college.college_managestaff'))
		

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
		
		q="insert into student values(null,'%s','%s','%s','%s','%s','%s','%s','college')"%(id,fname,lname,place,num,email,cid)

		insert(q)
		return redirect(url_for('college.college_managestaff'))

	return render_template('college_managestaff.html',data=data)

@college.route('/college_viewscho')
def college_viewscho():
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

		
		return redirect(url_for('college.college_viewscho'))


	if action=='update':
		q="update scholarship set status='accept' where scholarship_id='%s'"%(cid)
		update(q)
		
		return redirect(url_for('college.college_viewscho'))


	return render_template('college_viewscho.html',data=data)

@college.route('/college_viewrequest')
def college_viewrequest():
	data={}
	cid=request.args['cid']
	q="select * from request inner join student using (student_id) where scholarship_id='%s'"%(cid)
	res=select(q)
	data['seee']=res
	return render_template('college_viewrequest.html',data=data)