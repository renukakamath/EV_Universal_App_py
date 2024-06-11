from flask import * 
from database import* 
import uuid

api=Blueprint('api',__name__)

@api.route('/logins')
def logins():
	data={}
	u=request.args['username']
	p=request.args['password']
	q1="select * from login where username='%s' and `password`='%s'"%(u,p)
	print(q1)
	res=select(q1)
	if res:
		data['data']=res
		data['status']='success'
	else:
		data['status']='failed'
	return str(data)

@api.route('/Userregistration')
def Userregistration():
	data={}
	f=request.args['fname']
	l=request.args['lname']
	
	pl=request.args['place']
	
	ph=request.args['phone']
	e=request.args['email']
	la=request.args['lati']
	lo=request.args['logi']
	u=request.args['username']
	p=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(u,p)
	res=select(q)
	if res:
		data['status']='already'
	else:
		q="insert into login values(NULL,'%s','%s','User')"%(u,p)
		lid=insert(q)
		r="insert into user values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,f,l,pl,ph,e,la,lo)
		insert(r)
		print(r)
		data['status']="success"
	return str(data)


@api.route('/Sparepartsdeliveryboy')
def Sparepartsdeliveryboy():
	data={}
	f=request.args['fname']
	l=request.args['lname']
	
	pl=request.args['place']
	
	ph=request.args['phone']
	e=request.args['email']
	la=request.args['lati']
	lo=request.args['logi']
	u=request.args['username']
	p=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(u,p)
	res=select(q)
	if res:
		data['status']='already'
	else:
		q="insert into login values(null,'%s','%s','Mechanic')"%(un,p)
		id=insert(q)
		q="insert into mechanic values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(id,f,l,pl,ph,e,la,lo)
		insert(q)
		print(r)
		data['status']="success"
	return str(data)

@api.route('/Rechargebunk')
def Rechargebunk():
	data={}
	f=request.args['fname']
	pl=request.args['place']
	la=request.args['lati']
	lo=request.args['logi']
	u=request.args['username']
	p=request.args['password']
	
	q="select * from login where username='%s' and password='%s'"%(u,p)
	res=select(q)
	if res:
		data['status']='already'

	else:
		q="insert into login values(NULL,'%s','%s','Bunk')"%(u,p)
		lid=insert(q)
		r="insert into bunk values(NULL,'%s','%s','%s','%s','%s')"%(lid,f,pl,la,lo)
		insert(r)
		print(r)
		data['status']="success"
	return str(data)

@api.route('/ViewUserprofile')
def ViewUserprofile():
	data={}
	lid=request.args['lid']
	q="select * from user where login_id='%s'"%(lid)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="ViewUserprofile"
	return str(data)

@api.route('/Userprofile')
def Userprofile():
	data={}
	n=request.args['name']
	p=request.args['place']
	ph=request.args['Phone']
	e=request.args['email']
	ln=request.args['lname']
	lid=request.args['login_id']
	q="update user set first_name='%s',last_name='%s',place='%s',phone='%s',email='%s' where login_id='%s'"%(n,ln,p,ph,e,lid)
	update(q)
	data['status']='success'
	data['method']="Userprofile"
	return str(data)

@api.route('/ViewBunkmanageprofile')
def ViewBunkmanageprofile():
	data={}
	lid=request.args['lid']
	q="select * from bunk where login_id='%s'"%(lid)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="ViewBunkmanageprofile"
	return str(data)

@api.route('/Bunkmanageprofile')
def Bunkmanageprofile():
	data={}
	n=request.args['name']
	p=request.args['place']
	
	lid=request.args['login_id']
	q="update bunk set name='%s',place='%s' where login_id='%s'"%(n,p,lid)
	update(q)
	data['status']='success'
	data['method']="Bunkmanageprofile"
	return str(data)


@api.route('/ViewDeliverymanageprofile')
def ViewDeliverymanageprofile():
	data={}
	lid=request.args['lid']
	q="select * from sparepart where login_id='%s'"%(lid)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="ViewDeliverymanageprofile"
	return str(data)

@api.route('/Deliverymanageprofile')
def Deliverymanageprofile():
	data={}
	n=request.args['name']
	p=request.args['place']
	ph=request.args['Phone']
	e=request.args['email']
	ln=request.args['lname']
	lid=request.args['login_id']
	q="update sparepart set firstname='%s',lastname='%s',place='%s',phone='%s',email='%s' where login_id='%s'"%(n,ln,p,ph,e,lid)
	update(q)
	data['status']='success'
	data['method']="Deliverymanageprofile"
	return str(data)

@api.route('/ViewMechanicmanageprofile')
def ViewMechanicmanageprofile():
	data={}
	lid=request.args['lid']
	q="select * from mechanic where login_id='%s'"%(lid)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="ViewMechanicmanageprofile"
	return str(data)

@api.route('/Mechanicmanageprofile')
def Mechanicmanageprofile():
	data={}
	n=request.args['name']
	p=request.args['place']
	ph=request.args['Phone']
	e=request.args['email']
	ln=request.args['lname']
	lid=request.args['login_id']
	q="update mechanic set firstname='%s',lastname='%s',place='%s',phone='%s',email='%s' where login_id='%s'"%(n,ln,p,ph,e,lid)
	update(q)
	data['status']='success'
	data['method']="Mechanicmanageprofile"
	return str(data)

@api.route('/UserViewvehicle')
def UserViewvehicle():
	data={}
	q="SELECT * FROM vehicles INNER JOIN company USING (company_id)"
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)


@api.route('/UserBookNow')
def UserBookNow():
	data={}
	lid=request.args['login_id']
	amt=request.args['amount']
	vid=request.args['vid']

	q=" insert into request values(null,'%s',(select user_id from user where login_id='%s'),'%s',curdate(),'Pending')"%(vid,lid,amt)
	insert(q)
	print(q)
	data['status']='success'
	return str(data)


@api.route('/UserViewbookings')
def UserViewbookings():
	data={}
	lid=request.args['log_id']
	q="select * from request inner join vehicles using (vehicle_id) inner join user using (user_id) where login_id='%s'"%(lid)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)


@api.route('/Makepayment')
def Makepayment():
	data={}
	lid=request.args['login_id']
	amt=request.args['amount']
	rid=request.args['rid']

	q="insert into payment values(null,'%s','request','%s',curdate())"%(rid,amt)
	insert(q)
	print(q)
	q="update request set status='Paid' where request_id='%s'"%(rid)
	update(q)
	data['status']='success'
	return str(data)



@api.route('/viewbunk')
def viewbunk():
	data={}
	q="select * from bunk"
	res=select(q)
	if res:
		data['data']=res
		data['status']="success"
	
	return str(data)


@api.route('/searchbunk')	
def searchbunk():
	data={}
	search='%'+request.args['search']+'%'
	q="SELECT * FROM `bunk` where name like '%s'"%(search)
	res=select(q)
	print(q)
	if res:
		data['status']="success"
		data['data']=res

	else:
		data['status']="failed"
	
	return str(data)

@api.route('/Rechargerequest')
def Rechargerequest():
	data={}
	lid=request.args['log_id']
	b=request.args['bid']
	q="insert into rechargerequest values(null,(select user_id from user where login_id='%s'),'%s','0',curdate(),'Requested')"%(lid,b)
	insert(q)
	print(q)
	data['status']='success'
	return str(data)


@api.route('/UserViewrechargerequests')
def UserViewrechargerequests():
	data={}
	lid=request.args['log_id']
	q="select * from rechargerequest inner join bunk using (bunk_id) inner join user using (user_id) where user_id=(select user_id from user where login_id='%s')"%(lid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)


@api.route('/rate')
def rate():
	data={}
	lid=request.args['log_id']
	rid=request.args['rid']
	rating=request.args['rating']

	q="insert into rating values(null,(select user_id from user where login_id='%s'),'%s','%s',curdate())"%(lid,rid,rating)
	insert(q)
	data['status']='success'
	data['method']='rate'
	return str(data)



@api.route('/viewmechanic')
def viewmechanic():
	data={}
	q="select * from mechanic"
	res=select(q)
	if res:
		data['data']=res
		data['status']="success"
	
	return str(data)


@api.route('/searchmechanic')	
def searchmechanic():
	data={}
	search='%'+request.args['search']+'%'
	q="SELECT * FROM `mechanic` where firstname like '%s'"%(search)
	res=select(q)
	print(q)
	if res:
		data['status']="success"
		data['data']=res

	else:
		data['status']="failed"
	
	return str(data)


@api.route('/mechanicrequest')
def mechanicrequest():
	data={}
	lid=request.args['log_id']
	b=request.args['mid']
	q="insert into mechanicrequest values(null,(select user_id from user where login_id='%s'),'%s','0',curdate(),'Requested')"%(lid,b)
	insert(q)
	print(q)
	data['status']='success'
	return str(data)


@api.route('/UserViewrequest')
def UserViewrequest():
	data={}
	lid=request.args['log_id']
	q="select * from mechanicrequest inner join mechanic using (mechanic_id) inner join user using (user_id) where user_id=(select user_id from user where login_id='%s')"%(lid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return  str(data)



@api.route('/mrateing')
def mrateing():
	data={}
	lid=request.args['log_id']
	mid=request.args['rid']
	rating=request.args['rating']

	q="insert into rating values(null,(select user_id from user where login_id='%s'),'%s','%s',curdate())"%(lid,mid,rating)
	insert(q)

	print(q)
	data['status']='success'
	data['method']='rate'
	return str(data)


@api.route('/Cancelrequest')
def Cancelrequest():
	data={}
	mid=request.args['mid']
	q="update mechanicrequest set status='Canceled' where mechanic_id='%s'"%(mid)
	update(q)
	data['status']='success'
	return str(data)


@api.route('/viewspareparts')
def viewspareparts():
	data={}
	q="select * from sparepart"
	res=select(q)
	if res:
		data['data']=res
		data['status']="success"
	
	return str(data)


@api.route('/searchspareparts')	
def searchspareparts():
	data={}
	search='%'+request.args['search']+'%'
	q="SELECT * FROM `sparepart` where firstname like '%s'"%(search)
	res=select(q)
	print(q)
	if res:
		data['status']="success"
		data['data']=res

	else:
		data['status']="failed"
	
	return str(data)
@api.route('/UserViewporoduct')
def UserViewporoduct():
	data={}
	sid=request.args['spid']
	q="select * from product inner join sparepart using (sparepart_id) where sparepart_id='%s'"%(sid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)



@api.route('/BookCycle')
def BookCycle():
	data={}
	lid=request.args['login_id']
	qty=request.args['quantity']
	tot=request.args['total']
	sid=request.args['sid']
	pid=request.args['pid']
	q="select * from `order` where user_id=(select user_id from user where login_id='%s') and status='pending'"%(lid)
	res=select(q)
	
	if res:
		omid=res[0]['order_id']
	else:
		q="insert into `order` values(null,'%s',(select user_id from user where login_id='%s'),'0','pending')"%(sid,lid)
		omid=insert(q)
		print(q)
	q="select * from `oderdetails` where product_id='%s' and order_id='%s'"%(pid,omid)
	res=select(q)
	print(q)
	if res:
		odid=res[0]['detail_id']
		q="update `oderdetails` set quantity=quantity+'%s' , amount=amount+'%s' where detail_id='%s'"%(qty,tot,odid)
		update(q)
		print(q)
	else:
		w="insert into `oderdetails` values(null,'%s','%s','%s','%s',curdate())"%(omid,pid,qty,tot)
		insert(w)
	q="update `order` set total=total+'%s' where order_id='%s'"%(tot,omid)
	update(q)


	data['status']='success'
	return str(data)


@api.route('/UserViewordereditems')	
def UserViewordereditems():
	data={}
	lid=request.args['log_id']
	q="SELECT * FROM `order` INNER JOIN `oderdetails` USING (`order_id`) INNER JOIN `sparepart` USING (`sparepart_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `user` USING (user_id) where user_id=(select user_id from user where login_id='%s') "%(lid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)

@api.route('/Makepayments')
def Makepayments():
	data={}
	lid=request.args['login_id']
	amt=request.args['amount']
	oid=request.args['oid']
	q="insert into payment values(null,'%s','Productbooking','%s',curdate())"%(oid,amt)
	insert(q)
	q="update `order` set status='Paid' where order_id='%s'"%(oid)
	update(q)
	data['status']='success'
	return str(data)

@api.route('/rateings')
def rateings():
	data={}
	lid=request.args['log_id']
	oid=request.args['rid']
	rating=request.args['rating']

	q="insert into rating values(null,(select user_id from user where login_id='%s'),'%s','%s',curdate())"%(lid,oid,rating)
	insert(q)
	data['status']='success'
	data['method']='rate'
	return str(data)


@api.route('/complaint')	
def complaint():
	data={}
	lid=request.args['lid']
	c=request.args['complaint']
	q="insert into `complaint` values(null,(select user_id from user where login_id='%s'),'%s','pending',curdate())"%(lid,c)
	insert(q)
	print(q)
	data['status']="success"
	data['method']="complaint"
	return str(data)

@api.route('/viewcomplaints')
def viewcomplaints():
	data={}
	lid=request.args['lid']
	q="select * from complaint inner join user using (user_id) where login_id='%s'"%(lid)
	res=select(q)
	data['data']=res
	data['status']="success"
	data['method']="viewcomplaints"
	return str(data)





@api.route('/bunkcomplaint')	
def bunkcomplaint():
	data={}
	lid=request.args['log_id']
	c=request.args['complaint']
	q="insert into complaint values(null,'%s','%s','pending',curdate())"%(lid,c)
	insert(q)
	data['status']="success"
	data['method']="complaint"
	return str(data)

@api.route('/bunkviewcomplaints')
def bunkviewcomplaints():
	data={}
	lid=request.args['log_id']
	q="SELECT * FROM complaint INNER JOIN bunk ON `complaint`.user_id=`bunk`.login_id where  login_id='%s' "%(lid)
	res=select(q)
	print(q)
	data['data']=res
	data['status']="success"
	data['method']="viewcomplaints"
	return str(data)


@api.route('/boycomplaint')	
def boycomplaint():
	data={}
	lid=request.args['log_id']
	c=request.args['complaint']
	q="insert into complaint values(null,'%s','%s','pending',curdate())"%(lid,c)
	insert(q)
	print(q)
	data['status']="success"
	data['method']="complaint"
	return str(data)

@api.route('/boyviewcomplaints')
def boyviewcomplaints():
	data={}
	lid=request.args['log_id']
	q="SELECT * FROM complaint INNER JOIN sparepart ON `complaint`.user_id=`sparepart`.login_id where  login_id='%s' "%(lid)
	res=select(q)
	print(q)
	print(q)
	data['data']=res
	data['status']="success"
	data['method']="viewcomplaints"
	return str(data)



@api.route('/Mechaniccomplaint')	
def Mechaniccomplaint():
	data={}
	lid=request.args['log_id']
	c=request.args['complaint']
	q="insert into complaint values(null,'%s','%s','pending',curdate())"%(lid,c)
	insert(q)
	print(q)
	data['status']="success"
	data['method']="complaint"
	return str(data)

@api.route('/Mechanicviewcomplaints')
def Mechanicviewcomplaints():
	data={}
	lid=request.args['log_id']
	q="SELECT * FROM complaint INNER JOIN mechanic ON `complaint`.user_id=`mechanic`.login_id where  login_id='%s' "%(lid)
	res=select(q)
	print(q)
	print(q)
	data['data']=res
	data['status']="success"
	data['method']="viewcomplaints"
	return str(data)


@api.route('/Bunkviewrequest')
def Bunkviewrequest():
	data={}
	lid=request.args['log_id']
	q="select * from rechargerequest inner join bunk using (bunk_id) inner join user using (user_id) where  bunk.login_id='%s'"%(lid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)


@api.route('/Bunkviewpayment')
def Bunkviewpayment():
	data={}
	rid=request.args['request_id']
	lid=request.args['log_id']

	q="SELECT *,CONCAT(payment.`amount`) AS pamo,CONCAT (`payment`.`date`) AS pdate FROM `payment` INNER JOIN `rechargerequest` ON payment.`requested_id`=`rechargerequest`.`request_id`  INNER JOIN USER USING (user_id) where request_id='%s' and requestedfor='request'"%(rid)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)


@api.route('/Servicecharge')
def Servicecharge():
	data={}
	rid=request.args['rid']
	q="update rechargerequest set amount=amount+'100' where request_id='%s'"%(rid)
	update(q)
	data['status']='success'
	return str(data)


@api.route('/Mechanicviewrequest')
def Mechanicviewrequest():
	data={}
	lid=request.args['log_id']

	q="select * from mechanicrequest inner join mechanic using (mechanic_id) inner join user using (user_id) where mechanic.login_id='%s'"%(lid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return  str(data)

@api.route('/accept')
def accept():
	data={}
	mid=request.args['mid']
	q="update mechanicrequest set status='Accept' where mrequest_id='%s'"%(mid)
	update(q)
	data['status']='success'
	return str(data)


@api.route('/reject')
def reject():
	data={}
	mid=request.args['mid']
	q="update mechanicrequest set status='reject' where mrequest_id='%s'"%(mid)
	update(q)
	data['status']='success'
	return str(data)


@api.route('/Service')
def Service():
	data={}
	mid=request.args['mid']
	q="update mechanicrequest set servicceamount=servicceamount+'100' where mrequest_id='%s'"%(mid)
	update(q)
	data['status']='success'
	return str(data)


@api.route('/MechaincViewpayment')
def MechaincViewpayment():
	data={}
	mid=request.args['mechanic_id']
	lid=request.args['log_id']

	q="SELECT *,CONCAT(payment.`amount`) AS pamo,CONCAT (`payment`.`date`) AS pdate FROM `payment` INNER JOIN `mechanicrequest` ON payment.`requested_id`=`mechanicrequest`.`mrequest_id`  INNER JOIN USER USING (user_id) where mrequest_id='%s' "%(mid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)


@api.route('/Mechanicviewuser')
def Mechanicviewuser():
	data={}
	lid=request.args['lid']
	mid=request.args['mid']

	q="SELECT * FROM USER INNER JOIN `mechanicrequest` USING (user_id)  where mrequest_id='%s'"%(mid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return  str(data)


@api.route('/Deliveryviewrequest')	
def Deliveryviewrequest():
	data={}
	lid=request.args['log_id']
	q="SELECT * FROM `order` INNER JOIN `oderdetails` USING (`order_id`) INNER JOIN `sparepart` USING (`sparepart_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `user` USING (user_id)"
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)


@api.route('/pickup')
def pickup():
	data={}
	oid=request.args['oid']
	q="update `order` set status='PickUp' where order_id='%s'"%(oid)
	update(q)
	data['status']='success'
	return str(data)

@api.route('/DeliveryViewuser')
def DeliveryViewuser():
	data={}
	lid=request.args['lid']
	oid=request.args['oid']

	q="SELECT * FROM USER INNER JOIN `order` USING (user_id)  where order_id='%s'"%(oid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return  str(data)


@api.route('/Delivery')
def Delivery():
	data={}
	oid=request.args['oid']
	q="update `order` set status='Delivery' where order_id='%s'"%(oid)
	update(q)
	data['status']='success'
	return str(data)


@api.route('/DeliveryViewpayment')
def DeliveryViewpayment():
	data={}
	oid=request.args['oid']
	lid=request.args['log_id']

	q="SELECT *,CONCAT(payment.`amount`) AS pamo,CONCAT (`payment`.`date`) AS pdate FROM `payment` INNER JOIN `order` ON payment.`requested_id`=`order`.`order_id`  INNER JOIN USER USING (user_id) where order_id='%s' and requestedfor='Productbooking' "%(oid)
	res=select(q)
	print(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)

@api.route('/Delivery_addproduct',methods=['post','get'])
def Delivery_addproduct():
	data={}
	lid=request.form['lid']
	pname=request.form['Pname']
	stock=request.form['stock']
	rate=request.form['rate']
	img=request.files['image']
	path="static/uploads/"+str(uuid.uuid4())+img.filename
	img.save(path)
	q="insert into product values(null,'%s','%s','%s','%s','%s')"%(lid,pname,path,stock,rate)
	insert(q)
	print(q)
	data['status']='success'
	return str(data)

@api.route('/Bunkviewbestplace')
def Bunkviewbestplace():
	data={}
	lid=request.args['log_id']
	q="select * from bunk where login_id='%s'"%(lid)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	return str(data)


















		








	

	


		

