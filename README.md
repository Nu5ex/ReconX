# 🔍 ReconX – Herramienta de reconocimiento de dominios

**ReconX** es una herramienta en Python para realizar reconocimiento pasivo de dominios y subdominios. Realiza consultas WHOIS, obtiene registros DNS, enumera subdominios desde crt.sh y proporciona enlaces directos a plataformas OSINT como Shodan y Censys.

---

## 🧰 Funcionalidades

- 🕵️ WHOIS Lookup  
- 🌐 Resolución DNS (`A`, `AAAA`, `NS`, `MX`, `TXT`, `CNAME`)
- 🔎 Enumeración de subdominios vía [crt.sh](https://crt.sh)
- 🔌 Escaneo de puertos comunes con identificación de servicios
- 🌍 Enlaces a Shodan y Censys

---

## 📦 Requisitos

Instala las dependencias necesarias:

```bash
pip install whois dnspython requests
```
---

## 🚀 Uso
```bash
python ReconX.py <dominio o URL>
```
Ejemplo:
```bash
python ReconX.py https://www.ejemplo.com
```
---

## 🖥️ Salida de ejemplo


---

## 🛡️ Aviso legal
Esta herramienta está destinada exclusivamente a fines educativos, de aprendizaje o pruebas autorizadas.
No la utilices contra sistemas o dominios sin permiso.
El mal uso de esta herramienta puede violar leyes locales o internacionales.

---

## 🚧 Próximas mejoras
- Exportar resultados a archivo (.json, .txt)

- Escaneo de puertos completo (1-65535)

- Modo silencioso o detallado (CLI flags)

- Integración con APIs (SecurityTrails, VirusTotal, OTX)

- Interfaz web con Flask o Streamlit
