@echo off
cls

color 0a
echo ------------------
echo  Save Initalized
echo ------------------
color B
git add *
git commit -a -m "Automated (All) Save"
git push -u origin master
color 0a
echo ------------------
echo  Save Completed
echo ------------------
pause
exit