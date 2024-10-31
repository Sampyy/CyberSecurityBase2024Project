Link to the repo: https://github.com/Sampyy/CyberSecurityBase2024Project
1. Do python manage.py migrate
2. do python create_db.py
this is to create the base users with username password "bob:squarepants" and "alice:redqueen"
3. run server with python manage.py runserver

We are using security risks based on the OWASP 2021 list.

The site is a (very) basic site to send messages to other users and receive them.

Flaw 1: Injection
https://github.com/Sampyy/CyberSecurityBase2024Project/blob/716f22e5bf9e066589e28edb6107766b5d1bfb91/pages/views.py#L22
The send message database pushing is unfortunately left wide open for an sql injection attack. An attacker can run any sql commands on the database through the message, such as the one listed above in the comment to drop tables, and also to make the first user an admin. This is why any sql commands should never use strings with the message added as a part of it, since it allows the possibility of sql injection. Additionally we are using executescript instead of execute, which runs multiple sql queries.
Fixing the sql injection is luckily somewhat simple with new frameworks, instead of inserting into the script that we are running, we should use a parametrised way of saving the message, as shown in the comment with creating a new message, and then using msg.save() to commit it to the database. 
Fix url: https://github.com/Sampyy/CyberSecurityBase2024Project/blob/716f22e5bf9e066589e28edb6107766b5d1bfb91/pages/views.py#L18

Flaw 2: Broken access control
https://github.com/Sampyy/CyberSecurityBase2024Project/blob/716f22e5bf9e066589e28edb6107766b5d1bfb91/pages/views.py#L36
There's a view to render specific messages based on the messages ID, but it is currently completely open, meaning privacy is being leaked. Anyone can just go and scour through the specific message/id/ urls and view peoples private messages between each other. Looking through the messages doesn't even require you to be logged in, so it's alternatively not really traceable to specific users if the vulnerability is found out later.

The fix is in the comment above to check that the users id matches either sender or receiver, who actually are the people involved and who should be able to see the message. This is a pretty simple fix, but works well enough and stops nosy individuals from spying on personal messages.
Fix url: https://github.com/Sampyy/CyberSecurityBase2024Project/blob/716f22e5bf9e066589e28edb6107766b5d1bfb91/pages/views.py#L32

Flaw 3: Identification and authentication failures
https://github.com/Sampyy/CyberSecurityBase2024Project/blob/716f22e5bf9e066589e28edb6107766b5d1bfb91/pages/views.py#L56
Currently on user registration, we are not checking password at all for its strength. You could make an account with password "a", and the website would be completely okay with it. This would increase the risk that people have their accounts hacked through simple brute force attempts, and is why we should be validating passwords to at least be somewhat stronger. 
The fix is above in comments to add simple validation based on the django basic password validation options. It doesn't fully fix everything, but it's a start to protecting people from themselves. Having a minimum length and checking against the most common passwords helps. This is important since while programmers don't always have good safety knowledge to keep them safe, users certainly aren't better in that. If you let them use weak passwords, they will do it to make it easier for themselves (and hackers). 
Fix url: https://github.com/Sampyy/CyberSecurityBase2024Project/blob/716f22e5bf9e066589e28edb6107766b5d1bfb91/pages/views.py#L49


Flaw 4: security misconfiguration
https://github.com/Sampyy/CyberSecurityBase2024Project/blob/716f22e5bf9e066589e28edb6107766b5d1bfb91/pages/views.py#L56
The developer making the site must have missed their cup of coffee, or forgotten to make changes after testing. Currently every account created is an admin account, which would be horrible if people realize it and try to gain access to admin tools that are enabled. This would let them do much more than they should with the website.
Fix is above in comment, just create a regular user like intended. This stops attackers from being able to use their regularly created accounts for evil purposes. It's probably also a good idea to never add code to create users with admin powers, as the admin accounts are likely not needed to be created often enough to want to add the functionality (and the potential for mistakes and vulnerabilities with it). Creating them manually when needed would perhaps be safer?
Fix url: https://github.com/Sampyy/CyberSecurityBase2024Project/blob/716f22e5bf9e066589e28edb6107766b5d1bfb91/pages/views.py#L55


Flaw 5: insecure design 
https://github.com/Sampyy/CyberSecurityBase2024Project/blob/716f22e5bf9e066589e28edb6107766b5d1bfb91/pages/views.py#L65
The recovery system here works fine, but recovering with knowledge-based questions such as mothers' maiden name and whatnot is not considered secure. The information is too easily possible to be social engineered or just investigated for it to be used to grant recoveries. The issue lies with them being things that the person recovering knows, but they are not unique as others can also know them. The questions also lead to a lot of very basic answers that can be bruteforced (one, two, three, four) to the questions etc.
To fix this we should ditch the entire idea of recovering with these questions, and use something else. As an example, I added recovering through an email instead. Maybe checking that the email is correct shouldn't be in the check either to give a potential attacker less information on their attack and confirming emails related to usernames. Recovery through recovery codes could be another option to consider.
Fix url: https://github.com/Sampyy/CyberSecurityBase2024Project/blob/716f22e5bf9e066589e28edb6107766b5d1bfb91/pages/views.py#L69