from utils.api import *

class TikTokGen:
    def __init__(self, device: dict or None = None, proxies: str or None = None):
        self.proxies = proxies if proxies else None
        self.device  = device if device else Applog(self.proxies).register_device() #Xlog(self.proxies).validate_device()
        self.session = requests.Session()

    def __base_params(self, addon: dict = {}):
        return urlencode({
            "passport-sdk-version" : 17,
            "os_api"               : 25,
            "device_type"          : "SM-G973N",
            "ssmix"                : "a",
            "manifest_version_code": 160904,
            "dpi"                  : 320,
            "carrier_region"       : "IE",
            "uoo"                  : 0,
            "region"               : "US",
            "carrier_region_v2"    : 310,
            "app_name"             : "musically_go",
            "version_name"         : "16.9.4",
            "timezone_offset"      : 7200,
            "ts"                   : int(time.time()),
            "ab_version"           : "16.9.4",
            "pass-route"           : 1,
            "cpu_support64"        : "false",
            "pass-region"          : 1,
            "storage_type"         : 0,
            "ac2"                  : "wifi",
            "ac"                   : "wifi",
            "app_type"             : "normal",
            "host_abi"             : "armeabi-v7a",
            "channel"              : "googleplay",
            "update_version_code"  : 160904,
            "_rticket"             : int(time.time() * 1000),
            "device_platform"      : "android",
            "iid"                  : self.device["install_id"],
            "build_number"         : "16.9.4",
            "locale"               : "en",
            "op_region"            : "IE",
            "version_code"         : 160904,
            "timezone_name"        : "Africa/Harare",
            "cdid"                 : self.device["cdid"], 
            "openudid"             : self.device["openudid"], 
            "sys_region"           : "US",
            "device_id"            : self.device["device_id"],
            "app_language"         : "en",
            "resolution"           : "900*1600",
            "device_brand"         : "samsung",
            "language"             : "en",
            "os_version"           : "7.1.2",
            "aid"                  : 1340 
        })
        
    def __base_headers(self, params: str, payload: str) -> dict:
        sig = Utils._sig(
            params = params,
            body   = payload
        )
        
        return {
            "x-ss-stub"             : hashlib.md5(payload.encode()).hexdigest(),
            "accept-encoding"       : "gzip",
            "passport-sdk-version"  : "17",
            "sdk-version"           : "2",
            "x-ss-req-ticket"       : str(int(time.time() * 1000)),
            "x-gorgon"              : sig["X-Gorgon"],
            "x-khronos"             : sig["X-Khronos"],
            "cookie"                : f"store-idc=useast2a; store-country-code=id; store-country-code-src=did; install_id={self.device['install_id']}",
            "content-type"          : "application/x-www-form-urlencoded; charset=UTF-8",
            "host"                  : "api16-va.tiktokv.com",
            "connection"            : "Keep-Alive",
            "user-agent"            : "okhttp/3.10.0.1"
        }

    def __check_email(self, email: str) -> requests.Response:

        params  = self.__base_params()
        payload = f"mix_mode=1&email={Utils._xor(email)}&account_sdk_source=app"

        return self.session.post(
            url     = (
                "https://api16-va.tiktokv.com"
                    + "/passport/user/check_email_registered?"
                    + params
            ), 
            data    = payload, 
            headers = self.__base_headers(params, payload),
        )

    def main(self):
        # time.sleep(30)
        # email    = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10)) + "@gmail.com"
        for x in range(10):
            email    = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10)) + "@gmail.com"
            
            __check_email: requests.Response = self.__check_email(email)
            print(__check_email.json())


if __name__ == '__main__':

    start = time.time()
    TikTokGen().main()
    print(time.time() - start)
