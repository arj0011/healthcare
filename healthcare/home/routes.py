from flask import render_template,current_app,flash
from flask_mail import Message
from .forms import ContactForm
from .models import ContactUs
from . import home_bp
from ..extensions import db,mail

@home_bp.route('/')
def index():  
    return render_template('index.html')

@home_bp.route('/about-us')
def aboutus():
    return render_template('aboutus.html')

@home_bp.route('/contact-us',methods=['GET','POST'])
def contactus():
    form = ContactForm()
    if form.validate_on_submit():
        contact = ContactUs(
            name = form.name.data.strip(),
            email = form.email.data.strip(),
            subject = form.subject.data.strip(),
            message = form.message.data.strip()
        )
        db.session.add(contact)
        db.session.commit()

        recipient = 'arjun.choudhary@infobeans.com'
        subject = form.subject.data.strip()
        body = form.message.data.strip()

        # Create a Message object
        msg = Message(subject=subject, recipients=[recipient])
        msg.body = body
        # Send the email
        try:
            mail.send(msg)
            flash('Message send successsully','success')
            return redirect(url_for('home.contactus'))
        except Exception as e:
           current_app.logger.warning(f'Unexpected error: {str(e)}', exc_info=True)
           flash('Message not send','failed')

    return render_template('contactus.html',form=form)  