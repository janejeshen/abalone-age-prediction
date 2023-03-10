import streamlit as smt
import pickle as pkl
# loading in the model to predict on the data  
with open('abalone-age-prediction/abalone.pkl', 'rb')  as f:
    abalone_model = pkl.load(f)  

    
def welcome():  
    return 'welcome you all'  
    
# here, we will define the function which will make the prediction using the      # data which the user have imported  
def prediction1(sex,length, diameter, height, whole_wt, shucked_wt, viscera_wt, shell_wt):    
     
    prediction1 = abalone_model.predict(  
        [[sex,length, diameter, height, whole_wt, shucked_wt, viscera_wt, shell_wt]])  
    print(prediction1)  
    return prediction1  
        
    
# Here, this is the main function in which we will be defining our webpage   
def main():  
      # Now, we will give the title to out web page  
    smt.title("Abalone age prediction")  
        
    # Now, we will be defining some of the frontend elements of our web            # page like the colour of background and fonts and font size, the padding and    # the text to be displayed  
    html_temp = """  
    <!DOCTYPE html>
<html>
<body style="background-color:aquamarine;">
<style> body {
         background-color: rgb(20,30, 1);
      }</style>
</body>
</html>
    """  
        
    # Now, this line will allow us to display the front-end aspects we have   
    # defined in the earlier  
    smt.markdown(html_temp, unsafe_allow_html = True)  
        
    # Here, the following lines will create the text boxes in which the user can   
    # enter the data which is required for making the prediction   
    abalone_heightlength = smt.text_input ("sex ", " ")
    abalone_heightlength = smt.text_input ("length ", " ")  
    abalone_diameter = smt.text_input ("diameter", " ")  
    abalone_height = smt.text_input ("Height", " ")
    abalone_whole_wt = smt.text_input ("whole wt", "")  
    abalone_shucked_wt = smt.text_input ("shucked wt", " ")  
    abalone_viscera_wt = smt.text_input ("viscera wt", " ")  
    abalone_shell_wt = smt.text_input ("shell wt", " ")
    result = " "  
        
    # here, the below line will ensure that whenever the button named 'Predict' # is clicked, the prediction function that is defined earlier is called for making   # the prediction and it will also store it in the variable result  
    if smt.button ("Predict"):  
        result = prediction1 (sex, length, diameter, height, whole_wt,
                              shucked_wt, viscera_wt, shell_wt)  
    smt.success ('The output of the above is {}'.format(result))  
if __name__== '__main__':  
    main()  