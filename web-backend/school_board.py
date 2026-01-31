from flask import * 
from database import*
import uuid



school_board=Blueprint('school_board',__name__)

@school_board.route('/school_board_home')
def school_board_home():

	return render_template('school_board_home.html')


@school_board.route('/school_board_manageschool',methods=['post','get'])
def school_board_manageschool():
	data={}
	cid=session['login_id']
	


	q="select * from school where school_board_id='%s'  "%(cid)
	res=select(q)
	data['stafffview']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='delete':
		q="delete from school where school_id='%s'"%(cid)
		delete(q)
		return redirect(url_for('school_board.school_board_manageschool'))


	if action=='update':
		q="select * from school where school_id='%s'"%(cid)
		res=select(q)
		data['stafff']=res

	if "update" in request.form:
		fname=request.form['fname']
		
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		
		q="update school set fname='%s',place='%s',phone='%s',email='%s' where school_id='%s'"%(fname,place,num,email,cid)
		update(q)
		return redirect(url_for('school_board.school_board_manageschool'))
		

	if "stafff" in request.form:
		fname=request.form['fname']
		
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="insert into login values (null,'%s','%s','school')"%(uname,pwd)
		id=insert(q)
		
		q="insert into school values(null,'%s','%s','%s','%s','%s','%s')"%(id,cid,fname,place,num,email)

		insert(q)
		return redirect(url_for('school_board.school_board_manageschool'))
		

	return render_template('school_board_manageschool.html',data=data)


@school_board.route('/school_board_viewscho')
def school_board_viewscho():
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

		
		return redirect(url_for('school_board.school_board_viewscho'))


	if action=='update':
		q="update scholarship set status='accept' where scholarship_id='%s'"%(cid)
		update(q)
		
		return redirect(url_for('school_board.school_board_viewscho'))


	return render_template('school_board_viewscho.html',data=data)

@school_board.route('/school_board_viewrequest')
def school_board_viewrequest():
	data={}
	cid=request.args['cid']
	q="select * from request inner join student using (student_id) where scholarship_id='%s'"%(cid)
	res=select(q)
	data['seee']=res
	return render_template('school_board_viewrequest.html',data=data)