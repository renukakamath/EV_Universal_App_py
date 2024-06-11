from flask import * 
from database import*




admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():

	return render_template('admin_home.html')

@admin.route('/admin_managemechanics',methods=['post','get'])
def admin_managemechanics():

	data={}
	q="select * from mechanic"
	res=select(q)
	data['mechanicview']=res


	if "action" in request.args:
		action=request.args['action']
		mid=request.args['mid']

	else:action=None

	if action=='delete':
		q="delete from mechanic where mechanic_id='%s'"%(mid)
		delete(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managemechanics'))


	if action=='update':
		q="select * from mechanic where mechanic_id='%s'"%(mid)
		res=select(q)
		data['mechanicupdate']=res

		if "upset" in request.form:
			f=request.form['fname']
			l=request.form['lname']
			p=request.form['place']
			ph=request.form['phone']
			e=request.form['email']
			q="update mechanic set firstname='%s' ,lastname='%s',place='%s',phone='%s',email='%s' where mechanic_id='%s'"%(f,l,p,ph,e,mid)
			update(q)
			print(q)
			flash('successfully')
			return redirect(url_for('admin.admin_managemechanics'))
			

	if "mechanic" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		pla=request.form['place']
		pho=request.form['phone']
		e=request.form['email']
		la=request.form['lat']
		lo=request.form['lon']
		un=request.form['uname']
		p=request.form['pwd']


		q="insert into login values(null,'%s','%s','mechanic')"%(un,p)
		id=insert(q)
		q="insert into mechanic values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(id,f,l,pla,pho,e,la,lo)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managemechanics'))

	return render_template('admin_managemechanics.html',data=data)

@admin.route('/admin_viewcomplaint')
def admin_viewcomplaint():
	data={}
	q="select * from complaint"
	res=select(q)
	data['complaintview']=res
	return render_template('admin_viewcomplaint.html',data=data)



@admin.route('/admin_viewpayment')
def admin_viewpayment():
	data={}
	q="select * from payment"
	res=select(q)
	data['paymentview']=res
	return render_template('admin_viewpayment.html',data=data)


@admin.route('/admin_viewrating')
def admin_viewrating():
	data={}
	q="select * from rating inner join user using (user_id)"
	res=select(q)
	data['ratingview']=res

	return render_template('admin_viewrating.html',data=data)



@admin.route('/admin_viewspareparts')
def admin_viewspareparts():
	data={}
	q="select * from sparepart inner join login using (login_id)"
	res=select(q)
	data['sparepartsview']=res

	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:action=None

	if action=='accept':
		q="update login set usertype='Deliveryboy' where login_id='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewspareparts'))


	if action=='reject':
		q="update login set usertype='Reject' where login_id='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewspareparts'))
		
		
		
	return render_template('admin_viewspareparts.html',data=data)




@admin.route('/admin_viewuser')
def admin_viewuser():
	data={}
	q="select * from user"
	res=select(q)
	data['userview']=res

	return render_template('admin_viewuser.html',data=data)

@admin.route('/admin_sendreply',methods=['post','get'])
def admin_sendreply():

	if "sendreply" in request.form:
		cid=request.args['cid']
		reply=request.form['reply']
		q="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewcomplaint'))


	return render_template('admin_sendreply.html')
	

