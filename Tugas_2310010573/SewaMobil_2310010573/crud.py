# -*- coding: utf-8 -*-
import mysql.connector
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class crud_sewaMobil:

    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='sewamobil_2310010573'
        )

    # ================================
    # CRUD TABEL MEMBER
    # ================================
    def tambahMember(self, id_member, username, password, nama, alamat, email, telepon):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO member (id_member, username, password, nama, alamat, email, telepon)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        aksi.execute(sql, (id_member, username, password, nama, alamat, email, telepon))
        self.koneksi.commit()
        aksi.close()

    def updateMember(self, id_member, username, password, nama, alamat, email, telepon):
        aksi = self.koneksi.cursor()
        sql = """UPDATE member SET username=%s, password=%s, nama=%s, alamat=%s,
                 email=%s, telepon=%s WHERE id_member=%s"""
        aksi.execute(sql, (username, password, nama, alamat, email, telepon, id_member))
        self.koneksi.commit()
        aksi.close()

    def hapusMember(self, id_member):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM member WHERE id_member=%s", (id_member,))
        self.koneksi.commit()
        aksi.close()

    def dataMember(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from member order by id_member asc")
        return aksi.fetchall()

    def filterMember(self, cari):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("""
            SELECT * FROM member
            WHERE id_member LIKE %s OR username LIKE %s OR password LIKE %s
            OR nama LIKE %s OR alamat LIKE %s OR email LIKE %s OR telepon LIKE %s
            """,
            ([
                f"%{cari}%", # id_member
                f"%{cari}%", # username
                f"%{cari}%", # password
                f"%{cari}%", # nama
                f"%{cari}%", # alamat
                f"%{cari}%", # email
                f"%{cari}%"  # telepon
            ])
        )
        return aksi.fetchall()

    def cetakMember(self):
        aksi = self.koneksi.cursor()
        aksi.execute("select * from member")
        data = aksi.fetchall()
        barisData = [["Id Member", "Username", "Password", "Nama", "Alamat", "Email", "Telepon"]] + list(data)
        # print(barisData)
        fileLaporan = "Laporan Member.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
        isiData = Table(barisData, colWidths = [50, 65, 70, 80, 100, 90, 90])
        pdf.build([isiData])

    # ================================
    # CRUD TABEL MERK
    # ================================
    def tambahMerek(self, id_merek, merek):
        aksi = self.koneksi.cursor()
        aksi.execute("INSERT INTO merek (id_merek, merek) VALUES (%s, %s)", (id_merek, merek))
        self.koneksi.commit()
        aksi.close()

    def updateMerek(self, id_merek, merek):
        aksi = self.koneksi.cursor()
        aksi.execute("UPDATE merek SET merek=%s WHERE id_merek=%s", (merek, id_merek))
        self.koneksi.commit()
        aksi.close()

    def hapusMerek(self, id_merek):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM merek WHERE id_merek=%s", (id_merek,))
        self.koneksi.commit()
        aksi.close()

    def dataMerek(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from merek order by id_merek asc")
        return aksi.fetchall()

    def filterMerek(self, cari):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from merek where id_merek like %s or merek like %s",
        ([f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    def cetakMerek(self):
        aksi = self.koneksi.cursor()
        aksi.execute("select * from merek")
        data = aksi.fetchall()
        barisData = [["Id Merek", "Merek"]] + list(data)
        # print(barisData)
        fileLaporan = "Laporan Merek.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
        isiData = Table(barisData, colWidths = [60, 160])
        pdf.build([isiData])

    def cetakFilterMerek(self, cari):
        aksi = self.koneksi.cursor()
        aksi.execute("select * from merek where merek = %s", ([f"{cari}"]))
        data = aksi.fetchall()
        barisData = [["Id Merek", "Merek"]] + list(data)
        #print(barisData)
        fileLaporan = "Laporan Merek.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
        isiData = Table(barisData, colWidths = [60, 160])
        pdf.build([isiData])

    # ================================
    # CRUD TABEL MOBIL
    # ================================
    def tambahMobil(self, id_mobil, tanggal, id_merek, tipe, tahun, harga, lokasi, warna, keterangan, status):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO mobil (id_mobil, tanggal, id_merek, type, tahun, harga, lokasi, warna,
                 keterangan, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        data = (id_mobil, tanggal, id_merek, tipe, tahun, harga, lokasi, warna, keterangan, status)
        aksi.execute(sql, data)
        self.koneksi.commit()
        aksi.close()

    def updateMobil(self, id_mobil, tanggal, id_merek, tipe, tahun, harga, lokasi, warna, keterangan, status):
        aksi = self.koneksi.cursor()
        sql = """UPDATE mobil SET tanggal=%s, id_merek=%s, type=%s, tahun=%s, harga=%s, lokasi=%s, warna=%s,
                 keterangan=%s, status=%s WHERE id_mobil=%s"""
        data = (tanggal, id_merek, tipe, tahun, harga, lokasi, warna, keterangan, status, id_mobil)
        aksi.execute(sql, data)
        self.koneksi.commit()
        aksi.close()

    def hapusMobil(self, id_mobil):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM mobil WHERE id_mobil=%s", (id_mobil,))
        self.koneksi.commit()
        aksi.close()

    def dataMobil(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from mobil order by id_mobil asc")
        return aksi.fetchall()

    def filterMobil(self, cari):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("""
            SELECT * FROM mobil
            WHERE id_mobil LIKE %s OR tanggal LIKE %s OR id_merek LIKE %s
            OR type LIKE %s OR tahun LIKE %s OR harga LIKE %s
            OR lokasi LIKE %s OR warna LIKE %s OR keterangan LIKE %s OR status LIKE %s
            """,
            ([
                f"%{cari}%", # id_mobil
                f"%{cari}%", # tanggal
                f"%{cari}%", # id_merek
                f"%{cari}%", # type_mobil
                f"%{cari}%", # tahun
                f"%{cari}%", # harga
                f"%{cari}%", # lokasi
                f"%{cari}%", # warna
                f"%{cari}%", # keterangan
                f"%{cari}%"  # status
            ])
        )
        return aksi.fetchall()

    def cetakMobil(self):
        aksi = self.koneksi.cursor()
        aksi.execute("select * from mobil")
        data = aksi.fetchall()
        barisData = [["Id Mobil", "Tanggal", "Id Merek", "Type", "Tahun", "Harga", "Lokasi", "Warna", "Keterangan", "Status"]] + list(data)
        # print(barisData)
        fileLaporan = "Laporan Mobil.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
        isiData = Table(barisData, colWidths = [45, 65, 45, 45, 40, 65, 60, 35, 80, 40])
        pdf.build([isiData])

    def cetakFilterMobil(self, cari):
        aksi = self.koneksi.cursor()
        aksi.execute("select * from mobil where status = %s", ([f"{cari}"]))
        data = aksi.fetchall()
        barisData = [["Id Mobil", "Tanggal", "Id Merek", "Type", "Tahun", "Harga", "Lokasi", "Warna", "Keterangan", "Status"]] + list(data)
        # print(barisData)
        fileLaporan = "Laporan Mobil.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
        isiData = Table(barisData, colWidths = [45, 65, 45, 45, 40, 65, 60, 35, 80, 40])
        pdf.build([isiData])

    # ================================
    # CRUD TABEL ADMIN
    # ================================
    def tambahAdmin(self, id_admin, username, password):
        aksi = self.koneksi.cursor()
        aksi.execute("INSERT INTO admin (id_admin, username, password) VALUES (%s, %s, %s)",
                     (id_admin, username, password))
        self.koneksi.commit()
        aksi.close()

    def updateAdmin(self, id_admin, username, password):
        aksi = self.koneksi.cursor()
        aksi.execute("UPDATE admin SET username=%s, password=%s WHERE id_admin=%s",
                     (username, password, id_admin))
        self.koneksi.commit()
        aksi.close()

    def hapusAdmin(self, id_admin):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM admin WHERE id_admin=%s", (id_admin,))
        self.koneksi.commit()
        aksi.close()

    def dataAdmin(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from admin order by id_admin asc")
        return aksi.fetchall()

    def filterAdmin(self, cari):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from admin where id_admin like %s or username like %s or password like %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    def cetakAdmin(self):
        aksi = self.koneksi.cursor()
        aksi.execute("select * from admin")
        data = aksi.fetchall()
        barisData = [["Id Admin", "Username", "Password"]] + list(data)
        # print(barisData)
        fileLaporan = "Laporan Admin.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
        isiData = Table(barisData, colWidths = [60, 100, 170])
        pdf.build([isiData])

    # ================================
    # CRUD TABEL TAWAR
    # ================================
    def tambahTawar(self, id_pesan, id_member, id_mobil, tawar, tanggal, pesan, status):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO tawar (id_pesan, id_member, id_mobil, tawar, tanggal, pesan, status)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        aksi.execute(sql, (id_pesan, id_member, id_mobil, tawar, tanggal, pesan, status))
        self.koneksi.commit()
        aksi.close()

    def updateTawar(self, id_pesan, id_member, id_mobil, tawar, tanggal, pesan, status):
        aksi = self.koneksi.cursor()
        sql = """UPDATE tawar SET id_member=%s, id_mobil=%s, tawar=%s, tanggal=%s, pesan=%s,
                 status=%s WHERE id_pesan=%s"""
        aksi.execute(sql, (id_member, id_mobil, tawar, tanggal, pesan, status, id_pesan))
        self.koneksi.commit()
        aksi.close()

    def hapusTawar(self, id_pesan):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM tawar WHERE id_pesan=%s", (id_pesan,))
        self.koneksi.commit()
        aksi.close()

    def dataTawar(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from tawar order by id_pesan asc")
        return aksi.fetchall()

    def filterTawar(self, cari):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("""
            SELECT * FROM tawar
            WHERE id_pesan LIKE %s OR id_member LIKE %s OR id_mobil LIKE %s
            OR tawar LIKE %s OR tanggal LIKE %s OR pesan LIKE %s OR status LIKE %s
            """,
            ([
                f"%{cari}%", # id_pesan
                f"%{cari}%", # id_member
                f"%{cari}%", # id_mobil
                f"%{cari}%", # tawar
                f"%{cari}%", # tanggal
                f"%{cari}%", # pesan
                f"%{cari}%"  # status
            ])
        )
        return aksi.fetchall()

    def cetakTawar(self):
        aksi = self.koneksi.cursor()
        aksi.execute("select * from tawar")
        data = aksi.fetchall()
        barisData = [["Id Pesan", "Id Member", "Id Mobil", "Tawar", "Tanggal", "Pesan", "Status"]] + list(data)
        # print(barisData)
        fileLaporan = "Laporan Tawar.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
        isiData = Table(barisData, colWidths = [45, 65, 45, 60, 60, 90, 40])
        pdf.build([isiData])

    def cetakFilterTawar(self, cari):
        aksi = self.koneksi.cursor()
        aksi.execute("select * from tawar where status = %s", ([f"{cari}"]))
        data = aksi.fetchall()
        barisData = [["Id Pesan", "Id Member", "Id Mobil", "Tawar", "Tanggal", "Pesan", "Status"]] + list(data)
        # print(barisData)
        fileLaporan = "Laporan Tawar.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
        isiData = Table(barisData, colWidths = [45, 65, 45, 60, 60, 90, 40])
        pdf.build([isiData])
