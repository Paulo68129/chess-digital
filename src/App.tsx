import React, { useState } from 'react';
import './App.css';

// Define the props type for our component
type AppProps = object

// URL for a placeholder profile picture
const profilePictureUrl = 'https://media.licdn.com/dms/image/v2/D4D03AQFVmCCJ_mXEFQ/profile-displayphoto-shrink_400_400/B4DZdapZ7rH4Ag-/0/1749572493549?e=1755734400&v=beta&t=mU8NZSY1gv-iQNLfxhdskQCE9YhXAKRTd8PLbSo-w1k';

/**
 * Main App component.
 * This is a React functional component written in TypeScript.
 */
const App: React.FC<AppProps> = () => {
  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = () => {
    setIsLoading(true);
    // Simulate login process
    setTimeout(() => {
      setIsLoading(false);
      alert('Login realizado com sucesso!');
    }, 2000);
  };

  return (
    <div className="bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900 min-h-screen flex flex-col items-center justify-center p-6 text-white font-sans animate-fade-in">
      
      {/* Background decoration */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-blue-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse"></div>
        <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-purple-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse"></div>
      </div>

      <div className="relative w-full max-w-sm bg-gray-800/90 backdrop-blur-sm rounded-3xl shadow-2xl p-8 flex flex-col items-center border border-gray-700/50 animate-slide-up">
        
        {/* Facebook logo area */}
        <div className="mb-8 text-center">
          <div className="text-4xl font-bold text-blue-500 mb-2">facebook</div>
          <div className="w-16 h-1 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full mx-auto"></div>
        </div>

        {/* Title text */}
        <h1 className="text-2xl font-bold mb-8 text-center text-gray-100">
          Bem vindo ao Facebook
        </h1>

        {/* Profile image with enhanced styling */}
        <div className="relative mb-8">
          <div className="absolute inset-0 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full animate-pulse-ring"></div>
          <img
            src={profilePictureUrl}
            alt="Foto do perfil"
            className="relative w-32 h-32 rounded-full object-cover ring-4 ring-white/20 shadow-xl"
          />
          <div className="absolute -bottom-2 -right-2 w-8 h-8 bg-green-500 rounded-full border-4 border-gray-800 flex items-center justify-center">
            <div className="w-3 h-3 bg-white rounded-full"></div>
          </div>
        </div>

        {/* Login button with enhanced interactivity */}
        <button 
          onClick={handleLogin}
          disabled={isLoading}
          className="group relative w-full bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 disabled:from-gray-600 disabled:to-gray-700 text-white font-semibold py-4 px-6 rounded-xl transition-all duration-300 transform hover:scale-105 hover:shadow-lg active:scale-95 disabled:cursor-not-allowed disabled:transform-none"
        >
          <div className="flex items-center justify-center space-x-2">
            {isLoading ? (
              <>
                <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                <span>Entrando...</span>
              </>
            ) : (
              <>
                <svg className="w-5 h-5 transition-transform group-hover:translate-x-1" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
                <span>Entrar</span>
              </>
            )}
          </div>
          
          {/* Button shine effect */}
          <div className="absolute inset-0 rounded-xl bg-gradient-to-r from-transparent via-white/10 to-transparent transform -skew-x-12 -translate-x-full group-hover:translate-x-full transition-transform duration-700"></div>
        </button>

        {/* Additional options */}
        <div className="mt-6 text-center space-y-3">
          <button className="text-blue-400 hover:text-blue-300 text-sm font-medium transition-colors duration-200">
            Esqueceu a senha?
          </button>
          <div className="flex items-center space-x-4">
            <div className="flex-1 h-px bg-gray-600"></div>
            <span className="text-gray-400 text-xs">ou</span>
            <div className="flex-1 h-px bg-gray-600"></div>
          </div>
          <button className="text-gray-300 hover:text-white text-sm font-medium transition-colors duration-200 border border-gray-600 hover:border-gray-500 px-4 py-2 rounded-lg">
            Criar nova conta
          </button>
        </div>
      </div>

      {/* Footer */}
      <div className="mt-8 text-center text-gray-400 text-xs">
        <p>© 2025 Facebook Clone. Feito com React + TypeScript</p>
      </div>
    </div>
  );
};

export default App;