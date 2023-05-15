Creating an AWS SSL certificate for a custom domain with cloudns
================================================================

This allows the setup to be completely free. However, whilst you tend to have to learn more with the DIY approach, the path is usually not as easy! But that is why this wiki is here! :)


**Validation:**

AWS > AWS Certificate Manager > Request certificate > Public certificate > Fully qualified domain name: customdomainname.com, DNS validation > Request > copy the following information:
  CNAME name: _longhexadecimalstring1.customdomainname.com.
  CNAME value: _longhexadecimalstring2.alphabeticalstring.acm-validations.aws.

(For ACM, the following records allow initial domain ownership validation and also ongoing automated certificate renewal:)
cloudns > select your custom domain > CNAME > Add new record > 
  **Type**: CNAME

  **Host**: [_longhexadecimalstring1].customdomainname.com

(remove the full stop and remove the customdomainname.com because cloudns already have this filled in for you)
  
  **Points to**: [_longhexadecimalstring2.alphabeticalstring.acm-validations.aws]

(remove the full stop)

Hit **Save**!

Validation from AWS' end usually takes between 5-30+ minutes and will need you to refresh the page in order for you to find out the good news. So you really cant afford to use trial and error here!!! (hence why I documented it here)

**Value**: an alias that points to an AWS domain that ACM uses to automatically renew your certificate

**Name**: 

Whilst the ACM certificate says it will expire in 45 days, ACM automatically renews your certificate as long as the certificate is in use and your CNAME record remains in place. 

**Load balancing:**

This is the next and very complicated thing you will need to set up.

[I found this guide successful](https://hackernoon.com/getting-a-free-ssl-certificate-on-aws-a-how-to-guide-6ef29e576d22)

Here are some more guides to setting it up:
- https://medium.com/hackernoon/getting-a-free-ssl-certificate-on-aws-a-how-to-guide-6ef29e576d22
- https://www.howtogeek.com/devops/how-to-setup-free-ssl-certificates-using-aws-load-balancers/

It would be great to have it redirect all http traffic to https
