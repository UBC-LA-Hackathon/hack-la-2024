// app/page.js
"use client";
import Link from 'next/link';

const discussions = [
  { title: "Discussion 1" },
  { title: "Discussion 2" },
  { title: "Discussion 3" },
];

const Home = () => {
  return (
    <div className="flex h-screen bg-gray-100">
      {/* Left side (Discussion Titles) */}
      <div className="w-1/2 flex flex-col border-r border-gray-300 bg-white">
        <div className="p-4 bg-blue-500 text-white text-center font-bold">
          Discussion Titles
        </div>
        <div className="flex-1 p-4 overflow-y-auto">
          {/* Display discussion titles in a vertical list */}
          <div className="space-y-4">
            {discussions.map((discussion, index) => (
              <Link key={index} href={`/discussions/${index}`}>
                <div className="p-3 bg-gray-200 rounded-lg cursor-pointer hover:bg-gray-300">
                  {discussion.title}
                </div>
              </Link>
            ))}
          </div>
        </div>
      </div>

      {/* Right side (Empty for now, reserved for future content) */}
      <div className="w-1/2 p-4 bg-gray-50">
        {/* Future content can be placed here */}
      </div>
    </div>
  );
};

export default Home;
