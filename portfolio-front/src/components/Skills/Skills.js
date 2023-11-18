import { BadgeCheckIcon, ChipIcon } from "@heroicons/react/solid";
import React, { useRef, useState, useEffect } from "react";
import { mySkills } from "../../Data/skills";
import axios from "axios";

export default function Skills(props) {
  const [skills, setSkills] = useState([{ name: "" }]);

  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT fefege...",
  };
  useEffect(() => {
    axios
      .get(
        `http://${process.env.REACT_APP_IP}:${process.env.REACT_APP_PORT}/api/v1/languages/`,
        {
          headers: headers,
        }
      )
      .then(async (response) => {
        // If request is good...

        const data = await response.data;

        const tranformedData = data.map((skillData) => {
          return {
            name: skillData.name,
          };
        });

        setSkills(tranformedData);
      })
      .catch((error) => {
        console.log("error " + error);
      });
  }, []);

  return (
    <section id="skills">
      <div className="container px-5 py-10 mx-auto">
        <div className="text-center mb-20">
          <ChipIcon className="w-10 inline-block mb-4" />
          <h1 className="sm:text-4xl text-3xl font-medium title-font text-white mb-4">
            Skills &amp; Technologies
          </h1>
          <p className="text-base leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto">
            As a skilled professional, I bring a diverse range of expertise to
            the table. My proficiency spans across various technologies and
            domains, showcasing my capabilities in web development, programming
            languages, front-end and back-end frameworks, database management,
            version control, and responsive design. Explore below to see a
            detailed list of my specific skills and technologies.
          </p>
        </div>
        <div className="flex flex-wrap lg:w-4/5 sm:mx-auto sm:mb-2 -mx-4">
          {mySkills.map((skill) => (
            <div key={skill} className="p-2 sm:w-1/3 w-full">
              <div className="bg-gray-800 rounded flex p-4 h-full items-center">
                <BadgeCheckIcon className="text-green-400 w-6 h-6 flex-shrink-0 mr-4" />
                <span className="title-font font-medium text-white">
                  {skill}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
