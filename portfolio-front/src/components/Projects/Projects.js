import { CodeIcon } from "@heroicons/react/solid";
import React, { useRef, useState, useEffect } from "react";
import TextTruncate from "react-text-truncate"; // recommend
// import { projects } from "../../data";
// import axios from "axios";
import { myProjects } from "../../Data/Projects";
export default function Projects() {
  const [projects, setProjects] = useState([
    {
      code_link: "",
      live_link: "",
      image: "",
      description: "",
      title: "",
      stack: "",
      languages: "",
    },
  ]);
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT fefege...",
  };

  // useEffect(() => {
  //   axios
  //     .get(
  //       `http://${process.env.REACT_APP_IP}:${process.env.REACT_APP_PORT}/api/v1/projects/`,
  //       {
  //         headers: headers,
  //       }
  //     )
  //     .then(async (response) => {
  //       // If request is good...

  //       const data = await response.data;

  //       const tranformedData = data.map((projectData) => {
  //         return {
  //           code_link: projectData.code_link,
  //           live_link: projectData.live_link,
  //           image: projectData.image,
  //           description: projectData.description,
  //           title: projectData.title,
  //           stack: projectData.stack,
  //           languages: projectData.languages,
  //         };
  //       });
  //       console.log(tranformedData);
  //       setProjects(tranformedData);
  //     })
  //     .catch((error) => {
  //       console.log("error " + error);
  //     });
  // }, []);

  return (
    <section id="projects" className="text-gray-400 bg-gray-900 body-font">
      <div className="container px-5 py-10 mx-auto text-center lg:px-40">
        <div className="flex flex-col w-full mb-20">
          <CodeIcon className="mx-auto inline-block w-10 mb-4" />
          <h1 className="sm:text-4xl text-3xl font-medium title-font mb-4 text-white">
            Apps I've Built
          </h1>
          <p className="lg:w-2/3 mx-auto leading-relaxed text-base">
            The following are some of my projects
          </p>
        </div>
        <div className="flex flex-wrap -m-4 ">
          {myProjects.map((project) => (
            <a
              href={project.live_link}
              key={project.image}
              className="sm:w-1/2 w-100 p-4"
              target="_blank"
            >
              <div className="flex container relative">
                <img
                  alt="gallery"
                  className="absolute inset-0 w-full h-full object-cover object-center"
                  src={project.image}
                />
                <div className="px-8 py-10 relative z-10 w-full border-4 border-gray-800 bg-gray-900 opacity-0 hover:opacity-100">
                  <h2 className="tracking-widest text-sm title-font font-medium text-green-400 mb-1">
                    {project.languages}
                  </h2>
                  <h1 className="title-font text-lg font-medium text-white mb-3">
                    {project.title}
                  </h1>
                  <p className="leading-relaxed">
                    <TextTruncate line={4} text={project.description}  truncateText="…" />
                  </p>
                  <div className=" text-white">
                    <CodeIcon className="mx-auto inline-block w-6 mb-4" />
                    {project.code_link}
                  </div>
                </div>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
