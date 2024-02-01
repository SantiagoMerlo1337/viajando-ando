import React from "react";

const Home = () => {
    return (
        <main className="h-screen px-4">
            <div className="py-24">
                <h2 className="text-4xl font-black">
                    ENCONTRÁ A TUS COMPAÑEROS DE VIAJE
                </h2>
                <h2 className="text-xl font-bold">Buscá, planeá y viajá 😉</h2>
            </div>
            <button className="block p-5 px-10 mx-auto text-2xl font-semibold bg-green-400 rounded-full hover:bg-green-500">
                ¡Quiero viajar!
            </button>
        </main>
    );
};

export default Home;
