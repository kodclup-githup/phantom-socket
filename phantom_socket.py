#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         PHANTOM SOCKET PREMIUM v2.0                         ║
║                         Geliştirici: KodClup                                ║
║                                                                              ║
║  ETİK KULLANIM UYARISI:                                                      ║
║  Bu araç sadece eğitim amaçlı geliştirilmiştir. Yalnızca kendi              ║
║  laboratuvar ortamınızda ve izniniz olan sistemlerde kullanın.              ║
║  Yetkisiz sistemlerde kullanımı yasaktır ve yasal sorumluluk                ║
║  kullanıcıya aittir.                                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import socket
import threading
import time
import sys
import json
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import re

class Colors:
    """Terminal renk kodları"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    PURPLE = '\033[35m'
    ORANGE = '\033[33m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'

class PhantomSocketPremium:
    def __init__(self):
        self.open_ports = []
        self.closed_ports = []
        self.filtered_ports = []
        self.target = ""
        self.scan_results = {}
        self.start_time = None
        self.end_time = None
        
        # Kapsamlı port veritabanı
        self.port_database = {
            # Web Servisleri
            80: {"name": "HTTP", "service": "Web Server", "description": "Hypertext Transfer Protocol", "risk": "ORTA", 
                 "advice": "HTTPS'e yönlendirme yapın ve HTTP'yi devre dışı bırakın.", "category": "Web"},
            443: {"name": "HTTPS", "service": "Secure Web Server", "description": "HTTP over SSL/TLS", "risk": "DÜŞÜK", 
                  "advice": "SSL sertifikalarını güncel tutun ve güvenli cipher suites kullanın.", "category": "Web"},
            8080: {"name": "HTTP-Alt", "service": "Alternative HTTP", "description": "Alternative HTTP port", "risk": "ORTA", 
                   "advice": "Gereksizse kapatın, gerekirse HTTPS kullanın.", "category": "Web"},
            8443: {"name": "HTTPS-Alt", "service": "Alternative HTTPS", "description": "Alternative HTTPS port", "risk": "DÜŞÜK", 
                   "advice": "SSL yapılandırmasını kontrol edin.", "category": "Web"},
            
            # Dosya Transfer
            21: {"name": "FTP", "service": "File Transfer Protocol", "description": "Dosya Transfer Protokolü", "risk": "YÜKSEK", 
                 "advice": "FTP şifrelenmemiş veri aktarımı yapar. SFTP veya FTPS kullanın.", "category": "File Transfer"},
            22: {"name": "SSH/SFTP", "service": "Secure Shell", "description": "Güvenli Kabuk Erişimi", "risk": "ORTA", 
                 "advice": "Güçlü şifreler kullanın, key-based authentication tercih edin.", "category": "Remote Access"},
            990: {"name": "FTPS", "service": "FTP over SSL", "description": "Güvenli FTP", "risk": "DÜŞÜK", 
                  "advice": "SSL sertifikalarını güncel tutun.", "category": "File Transfer"},
            
            # E-posta Servisleri
            25: {"name": "SMTP", "service": "Simple Mail Transfer Protocol", "description": "E-posta Gönderme", "risk": "ORTA", 
                 "advice": "SMTP güvenlik ayarlarını kontrol edin ve TLS kullanın.", "category": "Email"},
            110: {"name": "POP3", "service": "Post Office Protocol v3", "description": "E-posta Alma", "risk": "YÜKSEK", 
                  "advice": "POP3S kullanın veya IMAP'e geçin.", "category": "Email"},
            143: {"name": "IMAP", "service": "Internet Message Access Protocol", "description": "E-posta Erişimi", "risk": "YÜKSEK", 
                  "advice": "IMAPS kullanın ve şifreleme aktif edin.", "category": "Email"},
            465: {"name": "SMTPS", "service": "SMTP over SSL", "description": "Güvenli SMTP", "risk": "DÜŞÜK", 
                  "advice": "SSL yapılandırmasını kontrol edin.", "category": "Email"},
            587: {"name": "SMTP-MSA", "service": "Mail Submission Agent", "description": "E-posta Gönderme (MSA)", "risk": "DÜŞÜK", 
                  "advice": "TLS kullanın ve kimlik doğrulama zorunlu tutun.", "category": "Email"},
            993: {"name": "IMAPS", "service": "IMAP over SSL", "description": "Güvenli IMAP", "risk": "DÜŞÜK", 
                  "advice": "Güvenli yapılandırma. Güçlü şifreler kullanın.", "category": "Email"},
            995: {"name": "POP3S", "service": "POP3 over SSL", "description": "Güvenli POP3", "risk": "DÜŞÜK", 
                  "advice": "Güvenli yapılandırma. Güçlü şifreler kullanın.", "category": "Email"},
            
            # Veritabanları
            1433: {"name": "MSSQL", "service": "Microsoft SQL Server", "description": "Microsoft SQL Server", "risk": "ÇOK YÜKSEK", 
                   "advice": "Veritabanını internete açmayın. VPN kullanın ve güçlü şifreler ayarlayın.", "category": "Database"},
            3306: {"name": "MySQL", "service": "MySQL Database", "description": "MySQL Veritabanı", "risk": "ÇOK YÜKSEK", 
                   "advice": "Veritabanını internete açmayın. Güçlü şifreler ve SSL kullanın.", "category": "Database"},
            5432: {"name": "PostgreSQL", "service": "PostgreSQL Database", "description": "PostgreSQL Veritabanı", "risk": "ÇOK YÜKSEK", 
                   "advice": "Veritabanını internete açmayın. SSL kullanın ve erişimi kısıtlayın.", "category": "Database"},
            6379: {"name": "Redis", "service": "Redis Database", "description": "Redis In-Memory Database", "risk": "ÇOK YÜKSEK", 
                   "advice": "Redis'i internete açmayın. Şifre koruması ve AUTH ekleyin.", "category": "Database"},
            27017: {"name": "MongoDB", "service": "MongoDB Database", "description": "MongoDB NoSQL Database", "risk": "ÇOK YÜKSEK", 
                    "advice": "MongoDB'yi internete açmayın. Kimlik doğrulama aktif edin.", "category": "Database"},
            
            # Uzak Erişim
            23: {"name": "Telnet", "service": "Telnet Protocol", "description": "Terminal Ağ Protokolü", "risk": "ÇOK YÜKSEK", 
                 "advice": "Telnet şifrelenmez! SSH kullanın ve Telnet'i devre dışı bırakın.", "category": "Remote Access"},
            3389: {"name": "RDP", "service": "Remote Desktop Protocol", "description": "Windows Uzak Masaüstü", "risk": "ÇOK YÜKSEK", 
                   "advice": "RDP'yi internete açmayın! VPN veya SSH tunnel kullanın.", "category": "Remote Access"},
            5900: {"name": "VNC", "service": "Virtual Network Computing", "description": "VNC Uzak Masaüstü", "risk": "ÇOK YÜKSEK", 
                   "advice": "VNC'yi internete açmayın! Şifreleme ve güçlü şifreler kullanın.", "category": "Remote Access"},
            5901: {"name": "VNC-1", "service": "VNC Display 1", "description": "VNC Display 1", "risk": "ÇOK YÜKSEK", 
                   "advice": "VNC'yi internete açmayın! Şifreleme kullanın.", "category": "Remote Access"},
            
            # DNS ve Ağ Servisleri
            53: {"name": "DNS", "service": "Domain Name System", "description": "Alan Adı Sistemi", "risk": "DÜŞÜK", 
                 "advice": "DNS amplification saldırılarına karşı koruma alın.", "category": "Network"},
            67: {"name": "DHCP", "service": "Dynamic Host Configuration Protocol", "description": "DHCP Server", "risk": "ORTA", 
                 "advice": "DHCP sunucusunu güvenli yapılandırın.", "category": "Network"},
            69: {"name": "TFTP", "service": "Trivial File Transfer Protocol", "description": "Basit Dosya Transfer", "risk": "YÜKSEK", 
                 "advice": "TFTP güvenli değildir. Gerekmedikçe kapatın.", "category": "File Transfer"},
            
            # Diğer Yaygın Servisler
            135: {"name": "RPC", "service": "Microsoft RPC", "description": "Windows RPC Endpoint Mapper", "risk": "YÜKSEK", 
                  "advice": "Gereksizse kapatın. Firewall ile koruyun.", "category": "Windows"},
            139: {"name": "NetBIOS", "service": "NetBIOS Session Service", "description": "NetBIOS Oturum Servisi", "risk": "YÜKSEK", 
                  "advice": "NetBIOS'u internete açmayın.", "category": "Windows"},
            445: {"name": "SMB", "service": "Server Message Block", "description": "Windows Dosya Paylaşımı", "risk": "ÇOK YÜKSEK", 
                  "advice": "SMB'yi internete açmayın! Güvenlik yamalarını uygulayın.", "category": "Windows"},
            161: {"name": "SNMP", "service": "Simple Network Management Protocol", "description": "Ağ Yönetim Protokolü", "risk": "YÜKSEK", 
                  "advice": "SNMP v3 kullanın ve community stringlerini değiştirin.", "category": "Network"},
            389: {"name": "LDAP", "service": "Lightweight Directory Access Protocol", "description": "Dizin Erişim Protokolü", "risk": "ORTA", 
                  "advice": "LDAPS kullanın ve erişimi kısıtlayın.", "category": "Directory"},
            636: {"name": "LDAPS", "service": "LDAP over SSL", "description": "Güvenli LDAP", "risk": "DÜŞÜK", 
                  "advice": "SSL sertifikalarını güncel tutun.", "category": "Directory"},
            
            # Uygulama Servisleri
            1521: {"name": "Oracle", "service": "Oracle Database", "description": "Oracle Veritabanı", "risk": "ÇOK YÜKSEK", 
                   "advice": "Veritabanını internete açmayın.", "category": "Database"},
            2049: {"name": "NFS", "service": "Network File System", "description": "Ağ Dosya Sistemi", "risk": "YÜKSEK", 
                   "advice": "NFS'i internete açmayın. Güvenli yapılandırın.", "category": "File Transfer"},
            3128: {"name": "Squid", "service": "Squid Proxy", "description": "HTTP Proxy Server", "risk": "ORTA", 
                   "advice": "Proxy ayarlarını güvenli yapılandırın.", "category": "Proxy"},
            5060: {"name": "SIP", "service": "Session Initiation Protocol", "description": "VoIP Protokolü", "risk": "ORTA", 
                   "advice": "SIP güvenlik ayarlarını kontrol edin.", "category": "VoIP"},
            6667: {"name": "IRC", "service": "Internet Relay Chat", "description": "IRC Server", "risk": "ORTA", 
                   "advice": "IRC sunucusunu güvenli yapılandırın.", "category": "Chat"},
        }

    def print_banner(self):
        """Gelişmiş araç başlığını yazdır"""
        banner = f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  {Colors.CYAN}██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗{Colors.PURPLE}           ║
║  {Colors.CYAN}██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║{Colors.PURPLE}           ║
║  {Colors.CYAN}██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║{Colors.PURPLE}           ║
║  {Colors.CYAN}██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║{Colors.PURPLE}           ║
║  {Colors.CYAN}██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║{Colors.PURPLE}           ║
║  {Colors.CYAN}╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝{Colors.PURPLE}           ║
║                                                                              ║
║  {Colors.YELLOW}███████╗ ██████╗  ██████╗██╗  ██╗███████╗████████╗{Colors.PURPLE}                      ║
║  {Colors.YELLOW}██╔════╝██╔═══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝{Colors.PURPLE}                      ║
║  {Colors.YELLOW}███████╗██║   ██║██║     █████╔╝ █████╗     ██║{Colors.PURPLE}                         ║
║  {Colors.YELLOW}╚════██║██║   ██║██║     ██╔═██╗ ██╔══╝     ██║{Colors.PURPLE}                         ║
║  {Colors.YELLOW}███████║╚██████╔╝╚██████╗██║  ██╗███████╗   ██║{Colors.PURPLE}                         ║
║  {Colors.YELLOW}╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝{Colors.PURPLE}                         ║
║                                                                              ║
║                     {Colors.BOLD}🔍 PREMIUM Port Tarama Aracı 🔍{Colors.PURPLE}                        ║
║                              {Colors.GREEN}Geliştirici: KodClup{Colors.PURPLE}                            ║
║                                {Colors.BLUE}Versiyon: 2.0 PREMIUM{Colors.PURPLE}                         ║
║                                                                              ║
║  {Colors.MAGENTA}✨ Premium Özellikler:{Colors.PURPLE}                                                ║
║  {Colors.WHITE}• Gelişmiş Servis Tanıma    • Hızlı Çoklu Thread Tarama{Colors.PURPLE}                ║
║  {Colors.WHITE}• Detaylı Güvenlik Analizi  • Kapsamlı Raporlama{Colors.PURPLE}                       ║
║  {Colors.WHITE}• Banner Grabbing           • JSON Export{Colors.PURPLE}                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.RED}⚠️  ETİK KULLANIM UYARISI ⚠️{Colors.END}
{Colors.YELLOW}Bu araç sadece eğitim amaçlı geliştirilmiştir.
Yalnızca kendi laboratuvar ortamınızda kullanın!{Colors.END}

"""
        print(banner)

    def get_risk_color(self, risk_level):
        """Risk seviyesine göre renk döndür"""
        colors = {
            "DÜŞÜK": Colors.GREEN,
            "ORTA": Colors.YELLOW,
            "YÜKSEK": Colors.ORANGE,
            "ÇOK YÜKSEK": Colors.RED,
            "BİLİNMİYOR": Colors.CYAN
        }
        return colors.get(risk_level, Colors.END)

    def grab_banner(self, host, port):
        """Banner grabbing - servis bilgisi alma"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((host, port))
            
            # HTTP servisleri için özel istek
            if port in [80, 8080, 8000, 8888]:
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            elif port in [443, 8443]:
                return "HTTPS/SSL Service"
            elif port == 21:
                pass  # FTP banner otomatik gelir
            elif port == 22:
                pass  # SSH banner otomatik gelir
            elif port == 25:
                pass  # SMTP banner otomatik gelir
            else:
                sock.send(b"\r\n")
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            sock.close()
            return banner[:200] if banner else "No banner"
        except:
            return "No banner"

    def advanced_port_scan(self, host, port):
        """Gelişmiş port taraması"""
        try:
            # TCP Connect Scan
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, port))
            
            if result == 0:
                # Port açık - banner grab
                banner = self.grab_banner(host, port)
                sock.close()
                
                port_info = {
                    'port': port,
                    'status': 'open',
                    'banner': banner,
                    'timestamp': datetime.now().strftime('%H:%M:%S')
                }
                
                if port in self.port_database:
                    port_info.update(self.port_database[port])
                else:
                    port_info.update({
                        'name': f'Unknown-{port}',
                        'service': 'Unknown Service',
                        'description': 'Tanımlanmamış servis',
                        'risk': 'BİLİNMİYOR',
                        'advice': 'Bu portu araştırın ve gereksizse kapatın.',
                        'category': 'Unknown'
                    })
                
                self.scan_results[port] = port_info
                self.open_ports.append(port)
                return True
            else:
                self.closed_ports.append(port)
                return False
                
        except socket.timeout:
            self.filtered_ports.append(port)
            return False
        except Exception:
            self.closed_ports.append(port)
            return False
        finally:
            try:
                sock.close()
            except:
                pass

    def threaded_scan(self, host, ports, max_threads=2000):
        """Gelişmiş çoklu thread tarama"""
        print(f"{Colors.CYAN}🔍 Gelişmiş tarama başlatılıyor...{Colors.END}")
        print(f"{Colors.BLUE}📡 Hedef: {host}{Colors.END}")
        print(f"{Colors.BLUE}🎯 Taranacak port sayısı: {len(ports)}{Colors.END}")
        print(f"{Colors.BLUE}🧵 Maksimum thread sayısı: {max_threads}{Colors.END}")
        print(f"{Colors.YELLOW}⏰ Başlangıç zamanı: {datetime.now().strftime('%H:%M:%S')}{Colors.END}\n")
        
        self.start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            # Progress tracking
            completed = 0
            total = len(ports)
            
            # Submit all tasks
            future_to_port = {
                executor.submit(self.advanced_port_scan, host, port): port 
                for port in ports
            }
            
            # Process completed tasks
            for future in as_completed(future_to_port):
                completed += 1
                port = future_to_port[future]
                
                try:
                    result = future.result()
                    if result:
                        print(f"{Colors.GREEN}[+] Port {port} - AÇIK{Colors.END}")
                except Exception as e:
                    print(f"{Colors.RED}[-] Port {port} tarama hatası: {e}{Colors.END}")
                
                # Progress bar
                progress = (completed / total) * 100
                bar_length = 50
                filled_length = int(bar_length * completed // total)
                bar = '█' * filled_length + '-' * (bar_length - filled_length)
                print(f"\r{Colors.CYAN}Progress: |{bar}| {progress:.1f}% ({completed}/{total}){Colors.END}", end='', flush=True)
        
        print()  # New line after progress bar
        self.end_time = time.time()

    def print_detailed_results(self):
        """Detaylı sonuçları yazdır"""
        scan_duration = self.end_time - self.start_time if self.end_time and self.start_time else 0
        
        print(f"\n{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║                              📊 DETAYLI TARAMA SONUÇLARI                     ║")
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        print(f"{Colors.GREEN}✅ Açık Portlar: {len(self.open_ports)}{Colors.END}")
        print(f"{Colors.RED}❌ Kapalı Portlar: {len(self.closed_ports)}{Colors.END}")
        print(f"{Colors.ORANGE}🔒 Filtrelenmiş Portlar: {len(self.filtered_ports)}{Colors.END}")
        print(f"{Colors.YELLOW}⏱️  Tarama Süresi: {scan_duration:.2f} saniye{Colors.END}")
        print(f"{Colors.YELLOW}⏰ Tarama Tamamlandı: {datetime.now().strftime('%H:%M:%S')}{Colors.END}\n")
        
        if self.open_ports:
            print(f"{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗")
            print(f"║                              🚨 AÇIK PORTLAR VE SERVİSLER 🚨                 ║")
            print(f"╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}\n")
            
            # Kategorilere göre grupla
            categories = {}
            for port in sorted(self.open_ports):
                if port in self.scan_results:
                    category = self.scan_results[port].get('category', 'Unknown')
                    if category not in categories:
                        categories[category] = []
                    categories[category].append(port)
            
            for category, ports in categories.items():
                print(f"{Colors.BOLD}{Colors.CYAN}📂 {category} Servisleri:{Colors.END}")
                print("─" * 80)
                
                for port in ports:
                    info = self.scan_results[port]
                    risk_color = self.get_risk_color(info['risk'])
                    
                    print(f"{Colors.GREEN}[+]{Colors.END} {Colors.BOLD}{info['service']} ({info['name']}) - Port {port}{Colors.END}")
                    print(f"    📝 Açıklama: {info['description']}")
                    print(f"    ⚠️  Risk Seviyesi: {risk_color}{info['risk']}{Colors.END}")
                    print(f"    🕒 Tespit Zamanı: {info['timestamp']}")
                    
                    if info['banner'] and info['banner'] != "No banner":
                        print(f"    🏷️  Banner: {Colors.CYAN}{info['banner'][:100]}...{Colors.END}")
                    
                    print(f"    💡 Güvenlik Önerisi: {Colors.YELLOW}{info['advice']}{Colors.END}")
                    print()
                
                print()
        
        # Risk analizi
        self.print_risk_analysis()
        
        # Güvenlik önerileri
        if self.open_ports:
            self.print_security_recommendations()
        else:
            print(f"{Colors.GREEN}🛡️  Tebrikler! Taradığımız portların hiçbiri açık değil.{Colors.END}")
            print(f"{Colors.GREEN}   Bu, sisteminizin dış saldırılara karşı iyi korunduğunu gösterir.{Colors.END}\n")

    def print_risk_analysis(self):
        """Risk analizi yazdır"""
        if not self.open_ports:
            return
            
        risk_counts = {"DÜŞÜK": 0, "ORTA": 0, "YÜKSEK": 0, "ÇOK YÜKSEK": 0, "BİLİNMİYOR": 0}
        
        for port in self.open_ports:
            if port in self.scan_results:
                risk = self.scan_results[port]['risk']
                risk_counts[risk] += 1
        
        print(f"{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║                              📈 RİSK ANALİZİ                                 ║")
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        total_risk_score = (risk_counts["DÜŞÜK"] * 1 + risk_counts["ORTA"] * 2 + 
                           risk_counts["YÜKSEK"] * 3 + risk_counts["ÇOK YÜKSEK"] * 4)
        
        for risk, count in risk_counts.items():
            if count > 0:
                color = self.get_risk_color(risk)
                print(f"{color}• {risk} Risk: {count} port{Colors.END}")
        
        print(f"\n{Colors.BOLD}📊 Toplam Risk Skoru: {total_risk_score}/100{Colors.END}")
        
        if total_risk_score >= 15:
            print(f"{Colors.RED}🚨 KRİTİK: Sisteminiz yüksek risk altında!{Colors.END}")
        elif total_risk_score >= 8:
            print(f"{Colors.ORANGE}⚠️  UYARI: Orta seviye risk tespit edildi.{Colors.END}")
        else:
            print(f"{Colors.GREEN}✅ İYİ: Risk seviyesi kabul edilebilir.{Colors.END}")
        
        print()

    def print_security_recommendations(self):
        """Gelişmiş güvenlik önerilerini yazdır"""
        print(f"{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║                           🛡️  DETAYLI GÜVENLİK ÖNERİLERİ                    ║")
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        # Genel öneriler
        general_recommendations = [
            "🔒 Kullanılmayan servisleri derhal kapatın",
            "🔑 Tüm servislerde güçlü şifreler ve 2FA kullanın",
            "🔄 Sistem güncellemelerini otomatik olarak yapın",
            "🛡️  Firewall kurallarını düzenli gözden geçirin",
            "📊 Log kayıtlarını merkezi olarak toplayın ve analiz edin",
            "🔐 VPN kullanarak uzaktan erişimi güvenli hale getirin",
            "⚡ Port bazlı erişim kontrolü uygulayın",
            "🔍 Düzenli güvenlik taramaları yapın",
            "📋 Incident response planı hazırlayın",
            "🎯 Penetration testing yaptırın"
        ]
        
        print(f"{Colors.CYAN}📋 Genel Güvenlik Önerileri:{Colors.END}")
        for rec in general_recommendations:
            print(f"   {Colors.YELLOW}{rec}{Colors.END}")
        
        # Spesifik öneriler
        if any(port in [21, 23, 80, 110, 143] for port in self.open_ports):
            print(f"\n{Colors.RED}🚨 ACİL EYLEM GEREKTİREN PORTLAR:{Colors.END}")
            for port in self.open_ports:
                if port in [21, 23, 3389, 5900] and port in self.scan_results:
                    info = self.scan_results[port]
                    print(f"   {Colors.RED}• Port {port} ({info['name']}): {info['advice']}{Colors.END}")
        
        print(f"\n{Colors.RED}⚠️  UYARI: Bu tarama sonuçlarını haftalık olarak tekrarlayın!{Colors.END}")
        print(f"{Colors.YELLOW}💡 Güvenlik bir süreç değil, sürekli bir durumdur.{Colors.END}\n")

    def export_results(self, filename=None):
        """Sonuçları JSON formatında export et"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"phantom_scan_{self.target}_{timestamp}.json"
        
        export_data = {
            "scan_info": {
                "target": self.target,
                "scan_time": datetime.now().isoformat(),
                "duration": self.end_time - self.start_time if self.end_time and self.start_time else 0,
                "total_ports_scanned": len(self.open_ports) + len(self.closed_ports) + len(self.filtered_ports)
            },
            "results": {
                "open_ports": len(self.open_ports),
                "closed_ports": len(self.closed_ports),
                "filtered_ports": len(self.filtered_ports)
            },
            "detailed_results": self.scan_results,
            "recommendations": "Detaylı güvenlik önerileri için raporu inceleyin."
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            print(f"{Colors.GREEN}✅ Sonuçlar başarıyla export edildi: {filename}{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}❌ Export hatası: {e}{Colors.END}")

    def clean_target(self, target):
        """Hedef URL'yi temizle ve sadece domain/IP kısmını al"""
        # HTTP/HTTPS protokollerini kaldır
        if target.startswith('http://'):
            target = target[7:]
        elif target.startswith('https://'):
            target = target[8:]
        
        # www. kısmını kaldır
        if target.startswith('www.'):
            target = target[4:]
        
        # Path kısmını kaldır (/ sonrasını)
        if '/' in target:
            target = target.split('/')[0]
        
        # Port kısmını kaldır (: sonrasını)
        if ':' in target and not target.replace('.', '').replace(':', '').isdigit():
            target = target.split(':')[0]
        
        return target.strip()

    def get_port_range(self, scan_type):
        """Tarama tipine göre port aralığı döndür"""
        port_ranges = {
            "quick": [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 1433, 3306, 3389, 5432, 5900, 6379, 8080, 27017],
            "common": list(range(1, 1001)) + [1433, 1521, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 27017],
            "full": list(range(1, 65536)),
            "web": [80, 443, 8000, 8080, 8443, 8888, 9000, 9090],
            "database": [1433, 1521, 3306, 5432, 6379, 27017, 50000],
            "remote": [22, 23, 3389, 5900, 5901, 5902]
        }
        return port_ranges.get(scan_type, port_ranges["quick"])

    def scan(self, target, scan_type="quick", export=False):
        """Ana tarama fonksiyonu"""
        # Hedefi temizle
        cleaned_target = self.clean_target(target)
        self.target = cleaned_target
        
        print(f"{Colors.BLUE}🔧 Girilen hedef: {target}{Colors.END}")
        if target != cleaned_target:
            print(f"{Colors.GREEN}🎯 Temizlenen hedef: {cleaned_target}{Colors.END}")
        
        # Port aralığını belirle
        ports = self.get_port_range(scan_type)
        
        try:
            # Hedef IP adresini çözümle
            target_ip = socket.gethostbyname(cleaned_target)
            print(f"{Colors.GREEN}✅ Hedef çözümlendi: {cleaned_target} → {target_ip}{Colors.END}\n")
            
            # Taramayı başlat
            self.threaded_scan(target_ip, ports)
            
            # Sonuçları yazdır
            self.print_detailed_results()
            
            # Export
            if export:
                self.export_results()
            
        except socket.gaierror:
            print(f"{Colors.RED}❌ Hata: '{cleaned_target}' alan adı çözümlenemedi!{Colors.END}")
            print(f"{Colors.YELLOW}💡 Lütfen geçerli bir alan adı veya IP adresi girin.{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}❌ Beklenmeyen hata: {str(e)}{Colors.END}")

def main():
    # Phantom Socket Premium'u başlat
    scanner = PhantomSocketPremium()
    scanner.print_banner()
    
    # Kullanıcıdan hedef al
    print(f"{Colors.CYAN}🎯 Hedef domain veya IP adresini girin: {Colors.END}", end="")
    target = input().strip()
    
    if not target:
        print(f"{Colors.RED}❌ Geçerli bir domain veya IP adresi girmelisiniz!{Colors.END}")
        return
    
    # Tarama tipi seç
    print(f"\n{Colors.CYAN}📋 Tarama tipini seçin:{Colors.END}")
    print(f"{Colors.YELLOW}1. Hızlı Tarama (Yaygın portlar){Colors.END}")
    print(f"{Colors.YELLOW}2. Standart Tarama (1-1000 + önemli portlar){Colors.END}")
    print(f"{Colors.YELLOW}3. Tam Tarama (1-65535){Colors.END}")
    print(f"{Colors.YELLOW}4. Web Servisleri{Colors.END}")
    print(f"{Colors.YELLOW}5. Veritabanı Servisleri{Colors.END}")
    print(f"{Colors.YELLOW}6. Uzak Erişim Servisleri{Colors.END}")
    
    scan_choice = input(f"{Colors.CYAN}Seçiminiz (1-6, varsayılan 1): {Colors.END}").strip()
    
    scan_types = {
        "1": "quick", "2": "common", "3": "full",
        "4": "web", "5": "database", "6": "remote"
    }
    scan_type = scan_types.get(scan_choice, "quick")
    
    # Export seçeneğiFt
    export_choice = input(f"{Colors.CYAN}Sonuçları JSON dosyasına export etmek istiyor musunuz? (e/h): {Colors.END}").lower()
    export = export_choice in ['e', 'evet', 'yes', 'y']
    
    # Kullanıcı onayı al
    print(f"{Colors.YELLOW}Bu aracı sadece kendi sistemlerinizde kullandığınızı onaylıyor musunuz? (e/h): {Colors.END}", end="")
    confirmation = input().lower()
    
    if confirmation in ['e', 'evet', 'yes', 'y']:
        print(f"{Colors.GREEN}✅ Onay alındı. Premium tarama başlatılıyor...\n{Colors.END}")
        scanner.scan(target, scan_type, export)
    else:
        print(f"{Colors.RED}❌ Tarama iptal edildi. Etik kullanım önemlidir!{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️  Tarama kullanıcı tarafından durduruldu.{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Kritik hata: {str(e)}{Colors.END}")