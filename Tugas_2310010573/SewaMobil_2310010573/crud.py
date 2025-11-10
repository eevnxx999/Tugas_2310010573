# -*- coding: utf-8 -*-
import mysql.connector

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
