# Proyek Akhir: Menyelesaikan Permasalahan Institut Pendidikan

## Business Understanding
Jaya Jaya Institute(JJI) merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini JJI telah mencetak banyak lulusan dengan reputasi yang sangat baik, Akan tetapi, terdapat banyak siswa yang tidak menyelesaikan pendidikannya alias _Drop out_


### Permasalahan Bisnis
* **Tingkat dropout yang tinggi** : Dengan jumlah _Drop out_ yang tinggi pada sebuah institusi pendidikan, akan berdampak antara lain menurunnya nilai akreditasi. Hal ini yang mengharuskan JJI mengambil tindakan untuk mendeteksi lebih dini kemungkinan siswa yang akan melakukan _Drop out_ sehingga dapat mengambil langkah yang tepat dan memberikan bimbingan khusus kepada mahasiswa

### Cakupan Proyek
Berdasarkan permasalahan yang telah di jelaskan, kita akan melakukan beberapa tahap berikut :
* Data Understanding, untuk mengumpulkan dan membersihkan data
* Data Preparation / Preprocessing, Menyaring data yang kurang relevan dan mengecek distribusi data yang memiliki korelasi tertentu dengan feature Status
* Modeling, melakukan pemodelan menggunakan 3 algoritma Machine Learning : Decision Tree, Random Forest, dan Gradient Boosting
* Evaluation, Mengevaluasi hasil dari pemodelan dan menyimpan model dengan akurasi tertinggi
* Business Dashboard untuk memantau perkembangan dan performa siswa
* Machine Learning Prototype untuk mendeteksi prediksi siswa melalui web sederhana

## Persiapan

Sumber data: [Dataset](https://doi.org/10.24432/C5MC89)

Setup environment:

* Aktifkan env dengan perintah berikut
```
myenv\Scripts\activate
```
install requirements
```
pip install -r requirements.txt
```

## Business Dashboard
Business Dashboard ini bertujuan menyajikan informasi terkait performa para siswa, dengan Dashboard ini dapat memudahkan JJI untuk memantau para siswa

* Informasi Umum & Analisis Distribusi : Menampilkan data Jumlah siswa, jumlah siswa yang melakukan drop out dan siswa yang lulus, jumlah pemegang beasiswa dan jumlah debitur, selain itu terdapat beberapa informasi distribusi terkait Gender, status Pernikahan, status Perpindahan, status siswa yang mendapat biaya terkini, nilai rata rata usia saat mendaftar berdasar siswa Drop out dan siswa Graduate, dan rata rata nilai kualifikasi sebelumnya, juga meliputi data terkait pilihan mode apllikasi para siswa
* Analisis performa pada semester awal : Meneliti jumlah kurikulum yang di ambil, kurikulum yang diminta dan nilai kurikulum pada semester awal
* Analisis performa pada semester kedua : Meneliti jumlah kurikulum yang di ambil, kurikulum yang diminta dan nilai kurikulum pada semester kedua

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.
Prototype machine learning ini dapat digunakan untuk memprediksi siswa yang dapat menyelesaikan pendidikan atau akan melakukan drop out

*Run the prototype*
1. Pastikan anda sudah menginstall streamlit
2. Buka Terminal atau CMD kemudian jalankan perintah berikut 
```
streamlit run student_predict.py
```

*Prototype link*
[Prediksi siswa]()

## Conclusion
Berdasarkan analisis yang telah dilakukan, dapat disimpulkan bahwa faktor-faktor pada data _Gender, Debtor, Marital_status, Displaced, Tuition_up_to_date, Scholarship_holder, Appliation_mode, Previous_qualification_grade,
Admission_grade, Age_at_enrollment, Curricular_units_1st_sem_enrolled, Curricular_units_1st_sem_approved, Curricular_units_1st_sem_grade, Curricular_units_2nd_sem_enrolled, Curricular_units_2nd_sem_evaluations, Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade, Curricular_units_2nd_sem_without_evaluations_ Sangat berpengaruh terhadap meningkatnya _Drop out_ para siswa,

**Marital status:** Pada korelasi status pernikahan dan tingkat drop out menunjukkan bahwa siswa dengan status lajang memliki potensi drop out yang lebih besar dibandingkan dengan status lainnya, beberapa kemungkinan seperti kurangnya support atau finansial yang belum stabil dapat membuat para siswa mengundurkan diri

**Debtor dan Shcholarship holder:** Hal yang menarik pada distribusi status debitur dan pemegang beasiswa, menunjukkan bahwa siswa dengan status debitur dan siswa yang memegang beasiswa memiliki tingkat drop out yang lebih rendah dibandingkan siswa non-debitur dan tanpa beasiswa. Hal ini menunjukkan bahwa siswa dengan kondisi keuangan mandiri baik dengan upaya sendiri(debitur) maupun bantuan eksternal(pemegang beasiswa) memiliki motivasi yang lebih besar untuk menyelesaikan pendidikan mereka

**Application mode:** Dalam mode pendaftaran pilihan, "over 23 years old" dikaitkan dengan tingkat putus sekolah yang lebih tinggi dibandingkan dengan mode pendaftaran lainnya, disusul "1st phase - general contignent" dan "2nd phase - general contignent"

**Prestasi Akademik:** Analisis mengungkapkan bahwa siswa dengan "Nilai Kualifikasi Sebelumnya" dan "Nilai Penerimaan" dalam rentang 120 hingga 140 lebih berpotensi melakukan drop out

**Age at enrollment**: Mayoritas siswa putus sekolah memulai studi mereka antara usia 20 dan 30 tahun, Pada usia ini siswa mungkin memiliki prioritas lain yang bersaing dengan pendidikan, seperti membangun karir. Hal ini dapat membuat mereka kesulitan untuk menyeimbangkan komitmen akademik dengan tanggung jawab lain 

**Evaluasi Mata Kuliah Semester 2:** Analisis menunjukkan bahwa siswa drop out memiliki 5 hingga 10 mata kuliah yang dievaluasi di Semester 2

**Kurikulum Semester:** Dalam jumlah kurikulum yang diambil pada semester 1 dan 2, siswa rata rata mengambil 4 hingga 5 mata kuliah per semester dengan tingkat kelulusan rata rata 4 mata kuliah, kemungkinan kemungkinan lain seperti terlalu banyaknya mata kuliah dan manajemen waktu yang kurang tepat membuat siswa kesulitan untuk menyerap materi dengan baik dapat meningkatkan tingkat drop out dan memperlambat kemajuan akademik mereka.

### Rekomendasi Action Items

- **Menerapkan Program Bantuan Keuangan Tertarget**: Berikan bantuan keuangan kepada siswa yang menghadapi kesulitan keuangan, seperti beasiswa, hibah, dan program kerja-studi. Hal ini dapat membantu mengurangi beban keuangan pada siswa dan membuat biaya sekolah lebih terjangkau
  
- **Menawarkan Program Intervensi Awal**:  Terapkan program intervensi awal yang mengidentifikasi siswa yang berisiko putus sekolah dan memberi mereka dukungan yang ditargetkan. Hal ini bisa termasuk program bimbingan belajar, konseling, dan mentoring
"# students_performance" 
