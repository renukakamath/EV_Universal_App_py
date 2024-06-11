from flask import *
from database import*


public=Blueprint('public',__name__)

@public.route('/')
def public_home():

	return render_template('public_home.html')

@public.route('/public_login',methods=['post','get'])
def public_login():
	if "login" in request.form:
		u=request.form['uname']
		p=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,p)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']
			lid=session['login_id']

			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.admin_home'))
			# elif res[0]['usertype']=="company":
			# 	q="select * from company where login_id='%s'"%(lid)
			# 	res=select(q)
			# 	if res:
			# 		session['company_id']=res[0]['company_id']
			# 		cid=session['company_id']
			# 	return redirect(url_for('company.company_home'))
		


		else:
			flash('invalid username and password')
					
	
					

		
	return render_template('public_login.html')


@public.route('/company_registration',methods=['post','get'])	
def company_registration():
	if "cusreg" in request.form:
		f=request.form['fname']
	
		p=request.form['place']
	
		n=request.form['num']
		e=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']


		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:

			flash('already exist')

		else:
			
			q="insert into login values(null,'%s','%s','company')"%(u,pa)
			id=insert(q)
			q="insert into company values(null,'%s','%s','%s','%s','%s')"%(id,f,p,n,e)
			insert(q)
			print(q)
			
			flash('successfully')
			return redirect(url_for('public.company_registration'))

	return render_template('company_registration.html')

		

