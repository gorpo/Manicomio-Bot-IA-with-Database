call heroku login
call heroku create --region us manicomio
call git init
call git add *
call git commit -m "Primeiro commit!"
call heroku git:remote -a manicomio
call git push heroku master
call heroku buildpacks:add --index 1 heroku-community/apt
call heroku ps:scale bot=1
call heroku logs --tail