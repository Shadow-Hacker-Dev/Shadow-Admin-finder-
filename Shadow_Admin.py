import os
os.system("pip install requests")
os.system ("pip install concurrent.futures")
os.system ("clear")
import requests
import concurrent.futures

red = '\033[31m'
green = '\033[32m'

# Logo 
print ('''

░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝
░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░
██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░

██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    ''')
print(f"{green}Shadow Admin finder tool in Python")
print("Developer @Shadow_Hackerz")

url = input("Enter the target link: ")

admin_pages = [
    "/admin/",
    "/admin-login.cfm",
    "/bb-admin/index.html",
    "/bb-admin/login.html",
    "/bb-admin/admin.html" , "/admin/", "/administrator/", "/admin1/", "/admin2/", "/admin3/", "/admin4/", "/admin5/" , "/usuarios/","/usuario/", "/administrator/", "/moderator/", "/webadmin/", "/adminarea/", "/bb-admin/", "/adminLogin/", "/admin_area/",
    "/panel-administracion/", "/instadmin/", "memberadmin/", "/administratorlogin/", "adm/" , "/admin/account.php" , "/admin/index.php" , "/admin/login.php" , "/admin/admin.php" , "/admin/account.php" , "admin_area/admin.php"  , "/admin_area/login.php"  , "/siteadmin/login.php"  , "/siteadmin/index.php"  , "/siteadmin/login.html"  , "/admin/account.html"  , "/admin/index.html"  , "/admin/login.html"  , "/admin/admin.php" , "/admin/account.php" , "/admin_area/admin.php"  , "/admin_area/login.php"  , "/siteadmin/login.php"  , "/siteadmin/index.php"  , "/siteadmin/login.html"  , "/admin/account.html"  , "/admin/index.html"  , "/admin/login.html"  , "/admin/admin.html"  , "/admin_area/index.php"  , "/bb-admin/index.php"  , "/bb-admin/login.php"  , "/bb-admin/admin.php" , "/admin/home.php"  , "/admin_area/login.html"  , "/admin_area/index.html"  , "/admin/controlpanel.php"  , "/admin.php"  , "/admincp/index.asp"  , "/admincp/login.asp"  , "/admincp/index.html"  , "/admin/account.html"  , "/adminpanel.html"  , "/webadmin.html"  , "/webadmin/index.html"  , "/webadmin/admin.html" , "/webadmin/login.html"  , "/admin/admin_login.html"  , "/admin_login.html"  , "/panel-administracion/login.html"  , "/admin/cp.php"  , "/cp.php"  , "/administrator/index.php"  , "/administrator/login.php"  , "/nsw/admin/login.php"  , "/webadmin/login.php"  , "/admin/admin_login.php"  , "/admin_login.php"  , "/administrator/account.php" , "/administrator.php"  , "/admin_area/admin.html"  , "/pages/admin/admin-login.php"  , "/admin/admin-login.php"  , "/admin-login.php"  , "/bb-admin/index.html"  , "/bb-admin/login.html"  , "/acceso.php"  , "/bb-admin/admin.html"  , "/admin/home.html"  , "/login.php"  , "/modelsearch/login.php"  , "/moderator.php" , "/moderator/login.php"  , "/moderator/admin.php"  , "/account.php"  , "/pages/admin/admin-login.html"  , "/admin/admin-login.html"  , "/admin-login.html"  , "/controlpanel.php"  , "/admincontrol.php"  , "/admin/adminLogin.html"  , "/adminLogin.html"  , "/admin/adminLogin.html"  , "/home.html"  , "/rcjakar/admin/login.php" , "/adminarea/index.html"  , "/adminarea/admin.html"  , "/webadmin.php"  , "/webadmin/index.php"  , "/webadmin/admin.php"  , "/admin/controlpanel.html"  , "/admin.html"  , "/admin/cp.html"  , "/cp.html"  , "/adminpanel.php"  , "/moderator.html"  , "/administrator/index.html"  , "/administrator/login.html" , "/user.html"  , "/administrator/account.html"  , "/administrator.html"  , "/login.html"  , "/modelsearch/login.html"  , "/moderator/login.html"  , "/adminarea/login.html"  , "/panel-administracion/index.html"  , "/panel-administracion/admin.html"  , "/modelsearch/index.html"  , "/modelsearch/admin.html"  , "/admincontrol/login.html"  , "/adm/index.html" , "/adm.html"  , "/moderator/admin.html"  , "/user.php"  , "/account.html"  , "/controlpanel.html"  , "/admincontrol.html"  , "/panel-administracion/login.php"  , "/wp-login.php"  , "/adminLogin.php"  , "/admin/adminLogin.php"  , "/home.php"  , "/admin.php"  , "/adminarea/index.php" , "/adminarea/admin.php"  , "/adminarea/login.php"  , "/panel-administracion/index.php"  , "/panel-administracion/admin.php"  , "/modelsearch/index.php"  , "/modelsearch/admin.php"  , "/admincontrol/login.php"  , "/adm/admloginuser.php"  , "/admloginuser.php"  , "/admin2.php"  , "/admin2/login.php"  , "/admin2/index.php"  , "/usuarios/login.php" , "/adm/index.php"  , "/adm.php"  , "/affiliate.php"  , "/adm_auth.php"  , "/memberadmin.php"  , "/administratorlogin.php"  , "/admin/"  , "/administrator/"  , "/admin1/"  , "/admin2/"  , "/admin3/"  , "/admin4/"  , "/admin5/" , "/moderator/"  , "/webadmin/"  , "/adminarea/"  , "/bb-admin/"  , "/adminLogin/"  , "/admin_area/"  , "/panel-administracion/"  , "/instadmin/"  , "/memberadmin/"  , "/administratorlogin/"  , "/adm/"  , "/account.asp"  , "/admin/account.asp" , "/admin/index.asp"  , "/admin/login.asp"  , "/admin/admin.asp"  , "/admin_area/admin.asp"  , "/admin_area/login.asp"  , "/admin/account.html"  , "/admin/index.html"  , "/admin/login.html"  , "/admin/admin.html"  , "/admin_area/admin.html"  , "/admin_area/login.html"  , "/admin_area/index.html"  , "/admin_area/index.asp"  , "/bb-admin/index.asp"  , "/bb-admin/login.asp"  , "/bb-admin/admin.asp"  , "/bb-admin/index.html" , "/bb-admin/login.html"  , "/bb-admin/admin.html"  , "/admin/home.html"  , "/admin/controlpanel.html"  , "/admin.html"  , "/admin/cp.html"  , "/cp.html"  , "/administrator/index.html"  , "/administrator/login.html"  , "/administrator/account.html"  , "/administrator.html"  , "/login.html"  , "/modelsearch/login.html" , "/moderator.html"  , "/moderator/login.html"  , "/moderator/admin.html"  , "/account.html"  , "/controlpanel.html"  , "/admincontrol.html"  , "/admin_login.html"  , "/panel-administracion/login.html"  , "/admin/home.asp"  , "/admin/controlpanel.asp"  , "/admin.asp"  , "/pages/admin/admin-login.asp"  , "/admin/admin-login.asp" , "/admin-login.asp"  , "/admin/cp.asp"  , "/cp.asp"  , "/administrator/account.asp"  , "/administrator.asp"  , "/acceso.asp"  , "/login.asp"  , "/modelsearch/login.asp"  , "/moderator.asp"  , "/moderator/login.asp"  , "/administrator/login.asp"  , "/moderator/admin.asp"  , "/controlpanel.asp" , "/admin/account.html"  , "/adminpanel.html"  , "/webadmin.html"  , "/pages/admin/admin-login.html"  , "/admin/admin-login.html"  , "/webadmin/index.html"  , "/webadmin/admin.html"  , "/webadmin/login.html"  , "/user.asp"  , "/user.html"  , "/admincp/index.asp"  , "/admincp/login.asp"  , "/admincp/index.html" , "/admin/adminLogin.html"  , "/adminLogin.html"  , "/admin/adminLogin.html"  , "/home.html"  , "/adminarea/index.html"  , "/adminarea/admin.html"  , "/adminarea/login.html"  , "/panel-administracion/index.html"  , "/panel-administracion/admin.html"  , "/modelsearch/index.html"  , "/modelsearch/admin.html"  , "/admin/admin_login.html"  , "/admincontrol/login.html" , "/adm/index.html"  , "/adm.html"  , "/admincontrol.asp"  , "/admin/account.asp"  , "/adminpanel.asp"  , "/webadmin.asp"  , "/webadmin/index.asp"  , "/webadmin/admin.asp"  , "/webadmin/login.asp"  , "/admin/admin_login.asp"  , "/admin_login.asp"  , "/panel-administracion/login.asp"  , "/adminLogin.asp" , "/admin/adminLogin.asp"  , "/home.asp"  , "/admin.asp"  , "/adminarea/index.asp"  , "/adminarea/admin.asp"  , "/adminarea/login.asp"  , "/admin-login.html"  , "/panel-administracion/index.asp"  , "/panel-administracion/admin.asp"  , "/modelsearch/index.asp"  , "/modelsearch/admin.asp"  , "/administrator/index.asp"  , "/admincontrol/login.asp" , "/adm/admloginuser.asp"  , "/admin2.asp"  , "/admin2/login.asp"  , "/admin2/index.asp"  , "/adm/index.asp"  , "/adm.asp"  , "/affiliate.asp"  , "/adm_auth.asp"  , "/memberadmin.asp"  , "/administratorlogin.asp"  , "/siteadmin/login.asp"  , "/siteadmin/index.asp"  , "/siteadmin/login.html" , "/admin/"  , "/administrator/"  , "/admin1/"  , "/admin2/"  , "/admin3/"  , "/admin4/"  , "/admin5/"  , "/usuarios/"  , "/usuario/"  , "/administrator/"  , "/moderator/"  , "/webadmin/"  , "/adminarea/" , "/bb-admin/"  , "/adminLogin/"  , "/admin_area/"  , "/panel-administracion/"  , "/instadmin/"  , "/memberadmin/"  , "/administratorlogin/"  , "/admin/account.cfm"  , "/adm/"  , "/admin/index.cfm"  , "/admin/login.cfm"  , "/admin/admin.cfm"  , "/admin/account.cfm" , "/admin_area/admin.cfm"  , "/admin_area/login.cfm"  , "/siteadmin/login.cfm"  , "/siteadmin/index.cfm"  , "/siteadmin/login.html"  , "/admin/account.html"  , "/admin/index.html"  , "/admin/login.html"  , "/admin/admin.html"  , "/admin_area/index.cfm"  , "/bb-admin/index.cfm"  , "/bb-admin/login.cfm"  , "/bb-admin/admin.cfm"   , "/admin/home.cfm"  , "/admin_area/login.html"  , "/admin_area/index.html" , "/admin/controlpanel.cfm"  , "/admin.cfm"  , "/admincp/index.asp"  , "/admincp/login.asp"  , "/admincp/index.html"  , "/admin/account.html"  , "/adminpanel.html"  , "/webadmin.html"  , "/webadmin/index.html"  , "/webadmin/admin.html"  , "/webadmin/login.html"  , "/admin/admin_login.html"  , "/admin_login.html" , "/panel-administracion/login.html"  , "/admin/cp.cfm"  , "/cp.cfm"  , "/administrator/index.cfm"  , "/administrator/login.cfm"  , "/nsw/admin/login.cfm"  , "/webadmin/login.cfm"  , "/admin/admin_login.cfm"  , "/admin_login.cfm"  , "/administrator/account.cfm"  , "/administrator.cfm"  , "/admin_area/admin.html"  , "/pages/admin/admin-login.cfm" , "/admin/admin-login.cfm"  , "/admin-login.cfm"  , "/bb-admin/index.html"  , "/bb-admin/login.html"  , "/bb-admin/admin.html"
]

found_admin_pages = 0

def check_admin_page(page):
    full_url = url + page
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(full_url, headers=headers)
        if response.history:
            print(f"{full_url} redirects to {response.url}")
        if response.status_code == 200:
            print(f"{green}[+] Admin page found: {full_url} (Status code {response.status_code})")
            print(f"{green}[+] Link: {response.url}")
            return full_url
        elif response.status_code in [401, 403]:
            print(f"{green}[+] Admin page found: {full_url}, but requires authentication (Status code {response.status_code})")
        else:
            print(f"{red}[-] {full_url} does not exist (Status code {response.status_code})")
    except requests.ConnectionError:
        print(f"{red}[!] {full_url} is unreachable")

print(f"{green}Starting the admin finder attack")
print(f"{red}powered by @Shadow_Hackerz")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    for page in admin_pages:
        futures.append(executor.submit(check_admin_page, page))
    for future in concurrent.futures.as_completed(futures):
        if future.result() is not None:
            found_admin_pages += 1

print(f"{green}Finished checking admin pages")

if found_admin_pages >= 1:
    print(f"{green}found {found_admin_pages} admin pages")
else:
    print(f"{red}found Zero Admin pages we are sorry")
