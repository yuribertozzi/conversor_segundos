segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")

total_segs = int(segundos_str)



dias = total_segs // 86400

segs_restantes_d = total_segs % 86400



horas = segs_restantes_d // 3600

segs_restantes_h = segs_restantes_d % 3600



minutos = segs_restantes_h // 60

segs_restantes_m = segs_restantes_h % 60



print(dias, "dias", horas, "horas", minutos, "minutos e", segs_restantes_m, "segundos.")

