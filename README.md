
# Next.js Dashboard Layout

Project ini adalah contoh struktur layout dashboard menggunakan **Next.js App Router**, dengan pemisahan komponen `Sidebar`, `Navbar`, dan `Root Layout` yang saling terhubung. Semua elemen sudah di-style menggunakan Tailwind CSS.

---

##  Fitur
- Layout global menggunakan `app/layout.js`
- Sidebar muncul di semua halaman
- Navbar berada di bagian atas secara full width
- Konten halaman otomatis ter-wrap dengan layout
- Komponen terpisah: `Sidebar.jsx` dan `Navbar.jsx`

---

##  Struktur Folder
```
app/
│── layout.js
│── page.js
│── globals.css
components/
│── Sidebar.jsx
│── Navbar.jsx
```

---

##  Kode Lengkap

### **app/layout.js**
```jsx
import Sidebar from "@/components/Sidebar";
import Navbar from "@/components/Navbar";
import "./globals.css";

export const metadata = {
  title: "Dashboard",
  description: "Dashboard with sidebar and navbar",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="flex h-screen">
        <Sidebar />

        <div className="flex flex-col flex-1">
          <Navbar />
          <main className="p-6 bg-gray-100 h-full">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
```

---

### **components/Sidebar.jsx**
```jsx
export default function Sidebar() {
  return (
    <aside className="w-64 bg-gray-900 text-white h-full p-6">
      <h2 className="text-xl font-bold mb-4">Sidebar</h2>
      <ul className="space-y-3">
        <li>Dashboard</li>
        <li>Users</li>
        <li>Settings</li>
      </ul>
    </aside>
  );
}
```

---

### **components/Navbar.jsx**
```jsx
export default function Navbar() {
  return (
    <nav className="w-full bg-pink-500 text-white p-4">
      <h1 className="text-lg font-semibold">Navbar</h1>
    </nav>
  );
}
```

---

### **app/page.js**
```jsx
export default function HomePage() {
  return (
    <div className="bg-white p-6 rounded-xl shadow">
      <h1 className="text-2xl font-bold mb-4">Home Page</h1>
      <p>Selamat datang di dashboard!</p>
    </div>
  );
}
```

---

##  Cara Menjalankan
```
npm install
npm run dev
```

---
