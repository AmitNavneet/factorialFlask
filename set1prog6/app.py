from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/factorial',methods=['POST'])
def factorial():
    num=int(request.form['num'])
    fact=1
    i=1
    calc=''
    while i<=num:
        fact=fact*i
        calc+=f'{i}'
        if i==num:
            calc+=f'={fact}'
        else:
            calc+='x'
        
        i=i+1
    
    return render_template('printFact.html',fact=fact,num=num,calc=calc)



if __name__=='__main__':
    app.run(debug=True)
