import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const GameDifficultyChart = () => {
  // Difficulty data based on the analysis
  const difficultyData = [
    { level: 1, royalMatch: 1, toonBlast: 1 },
    { level: 2, royalMatch: 1, toonBlast: 1 },
    { level: 3, royalMatch: 1, toonBlast: 2 },
    { level: 4, royalMatch: 2, toonBlast: 2 },
    { level: 5, royalMatch: 2, toonBlast: 2 },
    { level: 6, royalMatch: 2, toonBlast: 2 },
    { level: 7, royalMatch: 2, toonBlast: 2 },
    { level: 8, royalMatch: 3, toonBlast: 3 },
    { level: 9, royalMatch: 2, toonBlast: 2 },
    { level: 10, royalMatch: 3, toonBlast: 3 },
    { level: 11, royalMatch: 3, toonBlast: 3 },
    { level: 12, royalMatch: 3, toonBlast: 4 },
    { level: 13, royalMatch: 4, toonBlast: 5 },
    { level: 14, royalMatch: 3, toonBlast: 4 },
    { level: 15, royalMatch: 2, toonBlast: 5 },
    { level: 16, royalMatch: 2, toonBlast: 3 },
    { level: 17, royalMatch: 4, toonBlast: 4 },
    { level: 18, royalMatch: 3, toonBlast: 4 },
    { level: 19, royalMatch: 5, toonBlast: 3 },
    { level: 20, royalMatch: 4, toonBlast: 5 },
    { level: 21, royalMatch: 3, toonBlast: 5 },
    { level: 22, royalMatch: 3, toonBlast: 4 },
    { level: 23, royalMatch: 4, toonBlast: 4 },
    { level: 24, royalMatch: 4, toonBlast: 3 },
    { level: 25, royalMatch: 4, toonBlast: 5 },
    { level: 26, royalMatch: 4, toonBlast: 4 },
    { level: 27, royalMatch: 4, toonBlast: 5 },
    { level: 28, royalMatch: 4, toonBlast: 3 },
    { level: 29, royalMatch: 5, toonBlast: 5 },
    { level: 30, royalMatch: 4, toonBlast: 4 },
    { level: 31, royalMatch: 4, toonBlast: 2 },
    { level: 32, royalMatch: 3, toonBlast: 4 },
    { level: 33, royalMatch: 3, toonBlast: 3 },
    { level: 34, royalMatch: 5, toonBlast: 3 },
    { level: 35, royalMatch: 3, toonBlast: 4 },
    { level: 36, royalMatch: 4, toonBlast: 4 },
    { level: 37, royalMatch: 4, toonBlast: 4 },
    { level: 38, royalMatch: 3, toonBlast: 3 },
    { level: 39, royalMatch: 5, toonBlast: 4 },
    { level: 40, royalMatch: 5, toonBlast: 4 },
  ];

  // Calculate 10-level averages
  const averages = [
    {
      segment: "1-10",
      royalMatch: difficultyData.slice(0, 10).reduce((acc, item) => acc + item.royalMatch, 0) / 10,
      toonBlast: difficultyData.slice(0, 10).reduce((acc, item) => acc + item.toonBlast, 0) / 10
    },
    {
      segment: "11-20",
      royalMatch: difficultyData.slice(10, 20).reduce((acc, item) => acc + item.royalMatch, 0) / 10,
      toonBlast: difficultyData.slice(10, 20).reduce((acc, item) => acc + item.toonBlast, 0) / 10
    },
    {
      segment: "21-30",
      royalMatch: difficultyData.slice(20, 30).reduce((acc, item) => acc + item.royalMatch, 0) / 10,
      toonBlast: difficultyData.slice(20, 30).reduce((acc, item) => acc + item.toonBlast, 0) / 10
    },
    {
      segment: "31-40",
      royalMatch: difficultyData.slice(30, 40).reduce((acc, item) => acc + item.royalMatch, 0) / 10,
      toonBlast: difficultyData.slice(30, 40).reduce((acc, item) => acc + item.toonBlast, 0) / 10
    }
  ];

  return (
    <div className="w-full space-y-6">
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-lg font-semibold mb-4">Difficulty Progression (Levels 1-40)</h2>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={difficultyData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="level" />
            <YAxis domain={[0, 5]} ticks={[0, 1, 2, 3, 4, 5]} />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="royalMatch" name="Royal Match" stroke="#8884d8" activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="toonBlast" name="Toon Blast" stroke="#82ca9d" activeDot={{ r: 8 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-lg font-semibold mb-4">Average Difficulty by 10-Level Segments</h2>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={averages} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="segment" />
            <YAxis domain={[0, 5]} ticks={[0, 1, 2, 3, 4, 5]} />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="royalMatch" name="Royal Match" stroke="#8884d8" strokeWidth={2} />
            <Line type="monotone" dataKey="toonBlast" name="Toon Blast" stroke="#82ca9d" strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default GameDifficultyChart;
