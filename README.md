# ncbackup

backup some nc shit.

# Steps
確認 mask-resource.xlsx 為正確的所有app遮罩
透過 sep2app_fxr.py 生成所有app的遮罩 > 存放在appfxr
確認 user_applist.xlsx 為正確的所有使用者可使用app
透過 gen_user_fxr.py 產生所有使用者的app遮罩 > 存放在userfxr
