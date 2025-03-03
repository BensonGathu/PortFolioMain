import React from "react";
import About from "./components/About/About";
import Contact from "./components/Contact/Contact";
import Navbar from "./components/Navbar/Navbar";
import Projects from "./components/Projects/Projects";
import Skills from "./components/Skills/Skills";
import Certifications from "./components/Certifications/Certifications";
import Certifications2 from "./components/Certifications/Certifications2";

export default function App() {
  return (
    <main className="text-gray-400 bg-gray-900 body-font center">

      <Navbar />
      <About />
      <Certifications />
        
      <Certifications2 />
      <Projects />
      <Skills />
   
      <Contact />
    </main>
  );
}