import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell, LineChart, Line } from 'recharts';

const GameAnalysisDashboard = () => {
  // Move count data by game segment
  const moveCountData = [
    { name: 'Levels 1-10', royalMatch: 27.1, toonBlast: 41.2 },
    { name: 'Levels 11-20', royalMatch: 25.0, toonBlast: 24.5 },
    { name: 'Levels 21-30', royalMatch: 24.8, toonBlast: 28.1 },
    { name: 'Levels 31-40', royalMatch: 23.5, toonBlast: 29.3 },
  ];
  
  // Power-up usage data
  const rmPowerTools = [
    { name: 'TNT', value: 83 },
    { name: 'Propeller', value: 93 },
    { name: 'Rocket', value: 119 },
    { name: 'Light Ball', value: 40 }
  ];
  
  const tbPowerTools = [
    { name: 'Bomb', value: 70 },
    { name: 'Rocket', value: 110 },
    { name: 'Disco Ball', value: 135 }
  ];
  
  // Obstacle distribution
  const rmObstacles = [
    { name: 'Box', value: 480 },
    { name: 'Grass', value: 350 },
    { name: 'Plate', value: 450 },
    { name: 'Mail', value: 475 },
    { name: 'Egg', value: 275 }
  ];
  
  const tbObstacles = [
    { name: 'Balloon', value: 2100 },
    { name: 'Crate', value: 440 },
    { name: 'Bubble', value: 400 },
    { name: 'Carrot', value: 630 },
    { name: 'Colored-Balloon', value: 560 }
  ];
  
  // Difficulty curve data
  const difficultyData = [
    { level: '1-10', royalMatch: 1.7, toonBlast: 1.8 },
    { level: '11-20', royalMatch: 3.1, toonBlast: 3.6 },
    { level: '21-30', royalMatch: 3.9, toonBlast: 4.2 },
    { level: '31-40', royalMatch: 4.0, toonBlast: 3.6 },
  ];
  
  // Retention feature appearance
  const retentionData = [
    { name: 'Rating Request', royalMatch: 15, toonBlast: 11 },
    { name: 'New Environment', royalMatch: 30, toonBlast: 20 },
    { name: 'Consecutive Win System', royalMatch: 32, toonBlast: 24 },
    { name: 'Major Difficulty Spike', royalMatch: 19, toonBlast: 15 },
  ];
  
  // Key game metrics
  const keyMetricsData = [
    { name: 'Average Moves', royalMatch: 25.1, toonBlast: 30.7 },
    { name: 'Average Unused Moves', royalMatch: 8.0, toonBlast: 9.5 },
    { name: 'Average Hint Usage', royalMatch: 1.2, toonBlast: 0.0 },
    { name: 'New Booster Count', royalMatch: 5, toonBlast: 4 },
  ];
  
  // Color sets for charts
  const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8'];
  const royalMatchColor = '#8884d8';
  const toonBlastColor = '#82ca9d';

  return (
    <div className="w-full p-4 space-y-8">
      <h1 className="text-2xl font-bold text-center">Royal Match vs. Toon Blast: Comparative Analysis</h1>
      
      {/* Move Count Comparison */}
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-lg font-semibold mb-4">Average Move Count By Level Segment</h2>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={moveCountData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="royalMatch" name="Royal Match" fill={royalMatchColor} />
            <Bar dataKey="toonBlast" name="Toon Blast" fill={toonBlastColor} />
          </BarChart>
        </ResponsiveContainer>
      </div>
      
      {/* Power-up distribution */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg font-semibold mb-4">Royal Match: Power-up Distribution</h2>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={rmPowerTools}
                cx="50%"
                cy="50%"
                labelLine={true}
                outerRadius={100}
                fill="#8884d8"
                dataKey="value"
                nameKey="name"
                label={({name, percent}) => `${name} ${(percent * 100).toFixed(0)}%`}
              >
                {rmPowerTools.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
        
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg font-semibold mb-4">Toon Blast: Power-up Distribution</h2>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={tbPowerTools}
                cx="50%"
                cy="50%"
                labelLine={true}
                outerRadius={100}
                fill="#82ca9d"
                dataKey="value"
                nameKey="name"
                label={({name, percent}) => `${name} ${(percent * 100).toFixed(0)}%`}
              >
                {tbPowerTools.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
      
      {/* Difficulty Progression */}
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-lg font-semibold mb-4">Average Difficulty by Level Segment</h2>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={difficultyData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="level" />
            <YAxis domain={[0, 5]} />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="royalMatch" name="Royal Match" stroke={royalMatchColor} strokeWidth={2} />
            <Line type="monotone" dataKey="toonBlast" name="Toon Blast" stroke={toonBlastColor} strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      </div>
      
      {/* Key Metrics Comparison */}
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-lg font-semibold mb-4">Key Game Metrics</h2>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={keyMetricsData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="royalMatch" name="Royal Match" fill={royalMatchColor} />
            <Bar dataKey="toonBlast" name="Toon Blast" fill={toonBlastColor} />
          </BarChart>
        </ResponsiveContainer>
      </div>
      
      {/* Retention Features Timing */}
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-lg font-semibold mb-4">Retention Feature Introduction (Level Number)</h2>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={retentionData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="royalMatch" name="Royal Match" fill={royalMatchColor} />
            <Bar dataKey="toonBlast" name="Toon Blast" fill={toonBlastColor} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default GameAnalysisDashboard;
