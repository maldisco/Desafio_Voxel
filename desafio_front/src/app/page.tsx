"use client";

import Voxel from "../assets/voxel.png";
import Image from "next/image";
import { useState } from "react";

export default function Home() {
  const [validEmail, setValidEmail] = useState(true);

  function validateEmail(email: string) {
    const re = /\S+@\S+\.\S+/;

    setValidEmail(re.test(email));
  }

  return (
    <main className="w-full flex justify-center items-center">
      {/* NOME VOXEL */}
      <div className="w-4/6 text-center">
        <p className="text-9xl font-italiana">VOXEL</p>
      </div>

      {/* LOGO E FORMULÁRIO */}
      <div className="flex flex-col border-l-2 h-screen border-gray-100 items-center justify-center w-2/6">
        <Image src={Voxel} alt="Voxel" />
        <form className="w-full flex flex-col items-center justify-center m-20">
          <div className="grid gap-3 mb-6 p-2 w-4/6">
            <label className="block text-md font-medium"> E-mail </label>
            <input
              type="text"
              id="email"
              className="block p-2.5 bg-gray-100 border border-gray-300 text-gray-900 rounded-lg"
              onBlur={(e) => validateEmail(e.target.value)}
            />
            {!validEmail && (
              <p className="mt-2 text-sm text-red-600">
                <span className="font-medium">Formato de email inválido!</span>
              </p>
            )}
          </div>
          <div className="grid gap-3 mb-6 p-2 w-4/6">
            <label className="block text-md font-medium"> Senha </label>
            <input
              type="text"
              id="senha"
              className="block p-2.5 bg-gray-100 border border-gray-300 text-gray-900 rounded-lg"
            />
          </div>
          <button className="focus:outline-none text-black-100 bg-yellow-400 hover:bg-yellow-500 focus:ring-4 focus:ring-yellow-300 font-medium rounded-lg text-md px-20 py-3 mr-2 mb-2 mt-6 dark:focus:ring-yellow-900">
            Log In
          </button>
        </form>
      </div>
    </main>
  );
}
