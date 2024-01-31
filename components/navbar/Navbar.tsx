import React from 'react'
import viajandoAndoLogo from "/public/img/logo.png"
import Image from 'next/image'

const Navbar = () => {
  return (
    <div className='flex items-center justify-between px-6 py-3 bg-white shadow-lg'>
        <Image src={viajandoAndoLogo} alt='Viajando Ando Logo' width={220}></Image>
        <h2 className='text-lg'>Usuario</h2>
    </div>
  )
}

export default Navbar