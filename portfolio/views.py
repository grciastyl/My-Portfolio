from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def about_me_view(request):
    return render(request, 'portfolio/about.html')

def experience_view(request):
    return render(request, 'portfolio/experience.html')

def contact_view(request):
    if request.method == 'POST':  # means if the form is not empty
        # to send the email
        form = ContactForm(request.POST)
        # collect the data from the form
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            # Build the email
            message_body = (
                f'You have received a new message from your website contact form.\n\n'
                f'Name: {name}\n'
                f'Email: {email}\n\n'
                f'Message:\n{message}'                
            )

            # send the email
            try:
                send_mail(
                    "Email from portfolio", #Subject
                    message_body, #Message that the user wrote
                    email, # from email, the users email
                    ['chrisfsdiclass@gmail.com'] # where to send the email to (my email address)
                )
                # after sending the email, empty the form 
                form = ContactForm()
                return render(request, 'portfolio/contact.html', {'form': form})  
            except Exception as e:
                print(f'Error sending email: {e}') 

                return render(request, 'portfolio/contact.html', {'form': form})
            
            
        else:
            print("data" + name, email, message)
    else:
        form = ContactForm()
        return render(request, 'portfolio/contact.html', {'form': form})    



