from flask import Flask, render_template, request, jsonify, flash, redirect, url_for

# import fucntion from app
import app as service
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') or 'default_secret_key_if_not_set'


# Route untuk Home
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    res, err = service.login(username, password)
    if err != None:
        flash(f"{err}")
        return redirect(url_for("index"))
    elif len(res) > 0 and err == None:
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("index"))

@app.route("/form-register")
def form_register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    
    res, err = service.register(name, email, username, password)
    if err != None:
        flash(f"{err}")
        return redirect(url_for("index"))
    elif res:
        flash("register berhasil")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("register"))

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        res, err = service.delete(id)
        if err is not None:
            return jsonify({"error": str(err)}), 400
        elif res:
            return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/form-update/<int:id>", methods=["GET"])
def formUpdate(id):
    res, err = service.getDataId(id)
    if err is not None:
        flash(f"{err}")
        return redirect(url_for("dashboard"))
    
    user_data = {
        "id": res[0],
        "nama": res[1],
        "email": res[2],
        "username": res[3],
        "password": res[4]
    }

    return render_template("form_update.html", user=user_data)

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    id = request.form.get("id")
    name = request.form.get("name")
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    
    res, err = service.update(id, name, email, username, password)
    if err != None:
        flash(f"{err}")
        return redirect(url_for("formUpdate", id=id))
    elif res:
        flash("update berhasil")
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    res, err = service.getData()
    if err is not None:
        flash(f"{err}")
        return redirect(url_for("index"))
    
    users_data = [
        {"id": user[0], "nama":user[1], "email": user[2], "username": user[3], "password": user[4]}
        for user in res
    ]
    return render_template("dashboard.html", users=users_data)

if __name__ == '__main__':
    app.run(debug=True)
