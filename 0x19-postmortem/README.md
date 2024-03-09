This is a postmortem for the outage of my learning website, www.realmns.tech, on February 2nd.

## Issue Summary
The issue happened on Feb 2, 2024. It started at around 10:30 PM GMT and lasted 20 minutes until 10:50 PM GMT. It didn’t affect the users so much, but when I tried to access it, it was not responding and showed a page load error. The root cause of this outage was an invalid server configuration that I made while working on my 0x10. HTTPS SSL project.
![Mind Blown](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHB5a2lvaGhhZGhtOWgxcDhpMGVsMDB1cnBpNDFuaGhiYzd3MzVqYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5XqGhjDB48YqA/giphy.gif)

## Timeline (timezone GMT)
10:30 PM: Changed the configuration
10:32 PM: Outage begins
10:37 PM: An outage was detected when I tried to refresh the page
10:38 PM: I tried re-configuring the server, following all the steps on the intranet
10:45 PM: Successful configuration
10:49 PM: Restarted the server
10:50 PM: Worked even more modified and secured

## Root cause and resolution
It was around 10:30 PM, and I was locked into a flow state, making optimizations to my web server. One crucial improvement I wanted to implement was enabling HTTPS/SSL encryption to fortify the security of the site.  

Unfortunately, as I dove deeper into the configuration process, I hit a roadblock. I had meticulously configured the server settings, but upon testing, everything went awry. It dawned on me that I had made a critical oversight: I forgot to include the essential certificate file within the server's configuration. This missing piece was the culprit behind the error message staring back at me, and it ultimately caused my website to go offline. That's when the website outage began. This turned out to be a valuable learning experience. After some troubleshooting, I pinpointed the culprit – the missing certificate file. This oversight highlighted the importance of meticulousness when configuring server settings. With renewed focus, I located the certificate and incorporated it correctly. Upon retesting, the website sprang back to life, now boasting the robust security of HTTPS/SSL.

## Corrective and preventative measures
Preventive measures you can use in the future to avoid similar website outages due to certificate issues include, creating a checklist specifically for enabling HTTPS/SSL. This checklist should include all the necessary steps, like generating or obtaining a certificate, adding it to the server configuration, and verifying its installation. Following this checklist, each time will help ensure you don't miss any crucial steps. Always double-check your configuration files before applying any changes, especially when dealing with security-critical aspects like certificates.
