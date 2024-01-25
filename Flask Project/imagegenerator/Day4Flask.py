from flask import Flask,render_template,request
from openai import OpenAI


client = OpenAI(
    api_key="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"
)

app = Flask(__name__)


@app.route('/generate',methods=['GET','POST'])
def gpt():
    if request.method == "POST":

        prompt = request.form['userprompt']
        response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        )
        image_url = response.data[0].url
        print(image_url)

    # print(generated_text)
        return render_template('image.html',prompt=prompt,generated_url=image_url)
    
    return render_template('image.html',prompt='',generated_url='')
     
app.run(debug=True)