import React, { useRef, useState, useEffect } from "react";
import axios from "axios";
import {BensonCv} from '../../Data/BensonCv.pdf'
export default function About() {
  const [userInfo, setUserInfo] = useState([
    { avatar: "", title: "", bio: "", cv: "", user: "" },
  ]);
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT fefege...",
  };
  useEffect(() => {
    axios
      .get(
        `http://${process.env.REACT_APP_IP}:${process.env.REACT_APP_PORT}/api/v1/getUser/`,
        {
          headers: headers,
        }
      )
      .then(async (response) => {
        // If request is good...

        const data = await response.data;

        const tranformedData = data.map((userData) => {
          return {
            id: userData.id,
            avatar: userData.avatar,
            bio: userData.bio,
            cv: userData.cv,
            title: userData.title,
            user: userData.user,
          };
        });

        setUserInfo(tranformedData);
      })
      .catch((error) => {
        console.log("error " + error);
      });
  }, []);

  return (
    <section id="about">
      <div className="container mx-auto flex px-10 py-20 md:flex-row flex-col items-center">
        <div className="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
          <h1 className="title-font sm:text-4xl text-3xl mb-4 font-medium text-white">
            Hi, I'm Benson Gathu,
            <br className="hidden lg:inline-block" />a FullStack Developer.
          </h1>
          <p className="mb-8 leading-relaxed">
            A passionate Full Stack Developer with a strong skill set in
            developing and implementing scalable mobile and web applications using popular
            tools and frameworks like Django, React, and Flutter.... Additionally,
            I have a keen interest in DevOps practices.
          </p>
          <div className="flex justify-center">
            <a
              href="#contact"
              className="inline-flex text-white bg-green-500 border-0 py-2 px-6 focus:outline-none hover:bg-green-600 rounded text-lg"
            >
              Work With Me
            </a>
            <a
              href="#projects"
              className="ml-4 inline-flex text-gray-400 bg-gray-800 border-0 py-2 px-6 focus:outline-none hover:bg-gray-700 hover:text-white rounded text-lg"
            >
              See My Past Work
            </a>
            <a
              download
              target="_blank"
              href={{BensonCv}}
              className="ml-4  inline-flex text-white bg-red-700	 border-0 py-2 px-6 focus:outline-none hover:bg-red-900 hover:text-white rounded text-lg"
            >
              Download Resume
            </a>
          </div>
        </div>
        <div className="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
          <img
            className="object-cover object-center rounded"
            alt="hero"
            src="./coding.svg"
          />
        </div>
      </div>
    </section>
  );
}
