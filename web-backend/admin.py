from flask import * 
from database import*



admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():

	return render_template('admin_home.html')



@admin.route('/admin_manageschool',methods=['post','get'])
def admin_manageschool():
	data={}
	
	q="select * from school_board  "
	res=select(q)
	data['stafffview']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='delete':
		q="delete from school_board where school_board_id='%s'"%(cid)
		delete(q)
		return redirect(url_for('admin.admin_manageschool'))


	if action=='update':
		q="select * from school_board where school_board_id='%s'"%(cid)
		res=select(q)
		data['stafff']=res

	if "update" in request.form:
		fname=request.form['fname']
		
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		
		q="update school_board set fname='%s',place='%s',phone='%s',email='%s' where school_board_id='%s'"%(fname,place,num,email,cid)
		update(q)
		return redirect(url_for('admin.admin_manageschool'))
		

	if "stafff" in request.form:
		fname=request.form['fname']
		
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="insert into login values (null,'%s','%s','school_board')"%(uname,pwd)
		id=insert(q)
		
		q="insert into school_board values(null,'%s','%s','%s','%s','%s')"%(id,fname,place,num,email)

		insert(q)
		return redirect(url_for('admin.admin_manageschool'))

	return render_template('admin_manageschool.html',data=data)



@admin.route('/admin_manageuniversity',methods=['post','get'])
def admin_manageuniversity():
	data={}
	
	q="select * from university  "
	res=select(q)
	data['stafffview']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='delete':
		q="delete from university where university_id='%s'"%(cid)
		delete(q)
		return redirect(url_for('admin.admin_manageuniversity'))


	if action=='update':
		q="select * from university where university_id='%s'"%(cid)
		res=select(q)
		data['stafff']=res

	if "update" in request.form:
		fname=request.form['fname']
		
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		
		q="update university set fname='%s',place='%s',phone='%s',email='%s' where university_id='%s'"%(fname,place,num,email,cid)
		update(q)
		return redirect(url_for('admin.admin_manageuniversity'))
		

	if "stafff" in request.form:
		fname=request.form['fname']
		
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="insert into login values (null,'%s','%s','university')"%(uname,pwd)
		id=insert(q)
		
		q="insert into university values(null,'%s','%s','%s','%s','%s')"%(id,fname,place,num,email)

		insert(q)
		return redirect(url_for('admin.admin_manageuniversity'))

	return render_template('admin_manageuniversity.html',data=data)


@admin.route('/admin_Viewcolleges')
def admin_Viewcolleges():
	data={}
	q="select * from college"
	res=select(q)
	data['colleges']=res


	return render_template('admin_Viewcolleges.html',data=data)



@admin.route('/admin_managescategory',methods=['post','get'])
def admin_managescategory():
	data={}
	
	q="select * from category "
	res=select(q)
	data['annnoo']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='delete':
		q="delete from category where category_id='%s'"%(cid)
		delete(q)
		return redirect(url_for('admin.admin_managescategory'))


	if action=='update':
		q="select * from category where category_id='%s'"%(cid)
		res=select(q)
		data['stafff']=res

	if "update" in request.form:
		course=request.form['course']
		
		
		q="update category set category='%s' where category_id='%s'"%(course,cid)
		update(q)
		return redirect(url_for('admin.admin_managescategory'))
		

	if "addgallery" in request.form:
		course=request.form['course']
	
	
		q="insert into category values(null,'%s')"%(course)

		insert(q)
		return redirect(url_for('admin.admin_managescategory'))

	return render_template('admin_managescategory.html',data=data)


@admin.route('/admin_managenotification',methods=['post','get'])
def admin_managenotification():
	data={}
	
	q="select * from notification "
	res=select(q)
	data['annnoo']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='delete':
		q="delete from notification where notification_id='%s'"%(cid)
		delete(q)
		return redirect(url_for('admin.admin_managenotification'))


	if action=='update':
		q="select * from notification where notification_id='%s'"%(cid)
		res=select(q)
		data['stafff']=res

	if "update" in request.form:
		course=request.form['course']
		
		
		q="update notification set notification='%s' where notification_id='%s'"%(course,cid)
		update(q)
		return redirect(url_for('admin.admin_managenotification'))
		

	if "addgallery" in request.form:
		course=request.form['course']
	
	
		q="insert into notification values(null,'%s')"%(course)

		insert(q)
		return redirect(url_for('admin.admin_managenotification'))

	return render_template('admin_managenotification.html',data=data)



@admin.route('/admin_managescholarship',methods=['post','get'])
def admin_managescholarship():
	data={}
	coid=request.args['coid']
	q="select * from scholarship  where category_id='%s'"%(coid)
	res=select(q)
	data['annnoo']=res

	if "addgallery" in request.form:
		course=request.form['seat']
		sdate=request.form['sdate']
		edate=request.form['edate']
		
		q="insert into scholarship values(null,'%s','%s','%s','%s',curdate(),'pending')"%(coid,course,sdate,edate)
		insert(q)
		return redirect(url_for('admin.admin_managescholarship',coid=coid))

	return render_template('admin_managescholarship.html',data=data)



@admin.route('/admin_viewcourse')
def admin_viewcourse():
	data={}
	cid=request.args['cid']
	q="select * from course inner join college using (college_id) where college_id='%s'"%(cid)
	res=select(q)
	data['course']=res
	return render_template('admin_viewcourse.html',data=data)

@admin.route('/admin_viewseats')
def admin_viewseats():
	data={}
	cid=request.args['cid']

	q="select * from seats inner join course using(course_id) where course_id='%s' "%(cid)
	res=select(q)
	data['seat']=res
	return render_template('admin_viewseats.html',data=data)



@admin.route('/admin_viewrequest')
def admin_viewrequest():
	data={}
	cid=request.args['cid']
	q="select * from request inner join student using (student_id)  where scholarship_id='%s'"%(cid)
	res=select(q)
	data['addm']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
		rid=request.args['rid']
	else:
		action=None

	if action=='accept':
		q="update request set status='accept' where request_id='%s'"%(rid)
		update(q)

		
		return redirect(url_for('admin.admin_viewrequest',cid=cid))


	if action=='update':
		q="update request set status='accept' where request_id='%s'"%(rid)
		update(q)
		
		return redirect(url_for('admin.admin_viewrequest',cid=cid))
	return render_template('admin_viewrequest.html',data=data)


@admin.route('/admin_viewcomplaint')
def admin_viewcomplaint():
	data={}
	q="select * from complaint inner join student on student.login_id=complaint.parent_id"
	res=select(q)
	data['comp']=res
	return render_template('admin_viewcomplaint.html',data=data)


@admin.route('/admin_sendreply',methods=['post','get'])
def admin_sendreply():
	if "sendreply" in request.form:
		cid=request.args['cid']
		reply=request.form['reply']
		q="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
		update(q)
		return redirect(url_for('admin.admin_viewcomplaint'))
	return render_template('admin_sendreply.html')



