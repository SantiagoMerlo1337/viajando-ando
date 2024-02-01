import React from "react";
import viajandoAndoLogo from "/public/img/logo.png";
import Image from "next/image";
import Link from "next/link";
import { SignedIn, SignedOut, UserButton } from "@clerk/nextjs";

const Navbar = () => {
    return (
        <nav className="flex items-center justify-between px-10 py-3 bg-white shadow-lg">
            <Link href="/">
                <Image
                    src={viajandoAndoLogo}
                    alt="Viajando Ando Logo"
                    width={220}
                ></Image>
            </Link>

            <div className="flex gap-4">
                <SignedIn>
                    <UserButton afterSignOutUrl="/"></UserButton>
                </SignedIn>
                <SignedOut>
                    <Link href="/sign-in" className="text-lg">
                        Iniciar sesion
                    </Link>
                    <Link href="/sign-up" className="text-lg">
                        Registrarse
                    </Link>
                </SignedOut>
            </div>
        </nav>
    );
};

export default Navbar;
