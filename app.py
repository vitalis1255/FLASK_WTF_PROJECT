from flask import Flask, url_for, redirect, render_template, flash
from forms import SimpleWTFForm


app = Flask(__name__)

app.secret_key = 'wtf_form_izuchukwu_abuja'

@app.route('/')
def home():
  return redirect(url_for('wtf_form'))#redirect to wtf_form function


@app.route('/wtf-form', methods=["GET","POST"])
def wtf_form():
  form = SimpleWTFForm()
  if form.validate_on_submit():
    flash(f"Thank you, {form.username.data}! Validated securely with Flask-WTF")
    return redirect(url_for('wtf_form'))
  return render_template('simple_wtf.html',form=form)


if __name__ == '__main__':
  app.run(debug=True)