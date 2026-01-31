from flask import *
from database import *


api=Blueprint('api',__name__)

@api.route('/logins',methods=['get','post'])
def logins():
	data={}
	print("Haii")
	username=request.args['username']
	password=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(username,password)
	res=select(q)
	print(res)
	if res:
		data['method']='login'
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
		data['method']='login'
	return str(data)	


@api.route('/complaint')	
def complaint():
	data={}
	lid=request.args['lid']
	c=request.args['complaint']
	q="insert into `complaint` values(null,'%s','%s','pending',now())"%(lid,c)
	insert(q)
	print(q)
	data['status']="success"
	data['method']="complaint"
	return str(data)

@api.route('/viewcomplaints')
def viewcomplaints():
	data={}
	lid=request.args['lid']
	q="select * from complaint inner join student on student.login_id=complaint.parent_id where login_id='%s'"%(lid)
	res=select(q)
	data['data']=res
	data['status']="success"
	data['method']="viewcomplaints"
	return str(data)



@api.route('/viewscholarship')
def viewscholarship():
	data={}

	
	q="select * from scholarship  inner join category using (category_id)"
	
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'

	return str(data)


@api.route('/Viewnotification')
def Viewnotification():
	data={}

	
	q="select * from notification  "
	
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'

	return str(data)


@api.route('/sendrequest')
def sendrequest():
	data={}
	
	cid=request.args['sid']
	f=request.args['log_id']
	

	q="insert into request values (null,'%s',(select student_id from student where login_id='%s'),curdate(),'pending')"%(cid,f)
	insert(q)
	print(q)
		
	data['status']='success'
	data['methods']='sendrequest'
	return str(data)



@api.route('/Viewrequest')
def Viewrequest():
	data={}
	
	lid=request.args['log_id']
	q="select *,concat( request.date) as rdate ,concat(request.status) as rstatus from request   inner join scholarship using (scholarship_id) where    student_id=(select student_id from student where login_id='%s')"%(lid)
	res=select(q)
	print(q)
	data['data']=res
	data['status']="success"
	data['method']="Viewrequest"
	return str(data)
