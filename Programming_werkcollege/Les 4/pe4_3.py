def lang_genoeg(lengte):
    if int(lengte) >= 120:
        return 'Je bent lang genoeg'
    else:
        return 'Sorry je bent te klein'
print(lang_genoeg(120))