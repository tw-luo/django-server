rm hello_world/templates/index.html
rm -r hello_world/static/js
rm -r hello_world/static/css

cd AbilityTest/
git pull
cp build/index.html ../hello_world/templates/index.html
cp -r build/static/js ../hello_world/static/js
cp -r build/static/css ../hello_world/static/css

cd ..
git add .
git commit -m "获取最新的前端界面"
git push
