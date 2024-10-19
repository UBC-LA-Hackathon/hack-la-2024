"use client";

import React, { useState } from "react";

const Home = () => {
  const userName = "Your Name"; // Replace this with the authenticated user's name later

  // State to manage discussions and selected discussion
  const [discussions, setDiscussions] = useState([
    {
      title: "Discussion 1",
      replies: [
        { message: "Reply 1", name: "Alice", timestamp: new Date().toLocaleString() },
        { message: "Reply 2", name: "Bob", timestamp: new Date().toLocaleString() },
      ],
    },
    {
      title: "Discussion 2",
      replies: [
        { message: "This is the first reply to Discussion 2", name: "Charlie", timestamp: new Date().toLocaleString() },
      ],
    },
    {
      title: "Discussion 3",
      replies: [],
    },
  ]);

  const [selectedDiscussion, setSelectedDiscussion] = useState(null);
  const [replyInput, setReplyInput] = useState("");

  // Handle selecting a discussion title
  const handleSelectDiscussion = (index) => {
    setSelectedDiscussion(index);
  };

  // Handle typing a reply
  const handleReplyInputChange = (e) => {
    setReplyInput(e.target.value);
  };

  // Handle sending a reply
  const handleSendReply = () => {
    if (replyInput.trim() !== "" && selectedDiscussion !== null) {
      const updatedDiscussions = [...discussions];
      const newReply = {
        message: replyInput,
        name: userName, // Use the predefined name
        timestamp: new Date().toLocaleString(),
      };
      updatedDiscussions[selectedDiscussion].replies.push(newReply);
      setDiscussions(updatedDiscussions);
      setReplyInput(""); // Clear reply input
    }
  };

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Left side (Discussion Forum) */}
      <div className="w-1/2 flex flex-col border-r border-gray-300 bg-white">
        <div className="p-4 bg-blue-500 text-white text-center font-bold">
          Discussion Forum
        </div>
        <div className="flex-1 p-4 overflow-y-auto">
          {/* Display discussion titles */}
          {discussions.map((discussion, index) => (
            <div
              key={index}
              className="mb-4 p-3 bg-gray-200 rounded-lg cursor-pointer"
              onClick={() => handleSelectDiscussion(index)}
            >
              {discussion.title}
            </div>
          ))}
        </div>
      </div>

      {/* Right side (Selected Discussion and Replies) */}
      <div className="w-1/2 p-4 bg-gray-50">
        {selectedDiscussion !== null ? (
          <div className="flex flex-col">
            <div className="text-lg font-bold mb-4">
              {discussions[selectedDiscussion].title}
            </div>
            {/* Display replies */}
            <div className="flex-1 bg-gray-200 p-4 rounded-lg mb-4 overflow-y-auto">
              {discussions[selectedDiscussion].replies.length > 0 ? (
                discussions[selectedDiscussion].replies.map((reply, idx) => (
                  <div key={idx} className="mb-2 p-2 bg-white rounded-lg">
                    <div className="font-bold">{reply.name}</div>
                    <div className="text-gray-600 text-sm">{reply.timestamp}</div>
                    <div>{reply.message}</div>
                  </div>
                ))
              ) : (
                <div className="text-gray-500">No replies yet.</div>
              )}
            </div>
            {/* Reply input */}
            <div className="flex">
              <input
                type="text"
                value={replyInput}
                onChange={handleReplyInputChange}
                className="flex-1 p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
                placeholder="Type your reply..."
              />
              <button
                onClick={handleSendReply}
                className="ml-2 p-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
              >
                Reply
              </button>
            </div>
          </div>
        ) : (
          <div className="text-lg font-bold">
            Select a discussion to see replies
          </div>
        )}
      </div>
    </div>
  );
};

export default Home;
