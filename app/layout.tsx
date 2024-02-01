import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "../components/navbar/Navbar";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
    title: "Viajando Ando",
    description: "Conectá con gente que quiera viajar con y como vos 🛣️",
};

export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <html lang="es">
            <body className={inter.className}>
                <Navbar></Navbar>

                <div className="container mx-auto bg-slate-100">{children}</div>
            </body>
        </html>
    );
}
