import { useState } from "react";
import DeckGL from "@deck.gl/react";
import { GeoJsonLayer } from "@deck.gl/layers";
import Map from "react-map-gl/maplibre";
import "maplibre-gl/dist/maplibre-gl.css";

const sampleData = {
  type: "FeatureCollection",
  features: [
    {
      type: "Feature",
      properties: { disease: "Fungal Blight" },
      geometry: {
        type: "Polygon",
        coordinates: [[
          [83.29, 17.71],
          [83.31, 17.71],
          [83.31, 17.73],
          [83.29, 17.73],
          [83.29, 17.71]
        ]]
      }
    },
    {
      type: "Feature",
      properties: { disease: "Leaf Spot" },
      geometry: {
        type: "Polygon",
        coordinates: [[
          [83.32, 17.71],
          [83.34, 17.71],
          [83.34, 17.73],
          [83.32, 17.73],
          [83.32, 17.71]
        ]]
      }
    }
  ]
};

function MapView() {
  const [showFungal, setShowFungal] = useState(true);
  const [showLeaf, setShowLeaf] = useState(true);

  const layers = [
    new GeoJsonLayer({
      id: "fungal-blight",
      data: sampleData.features.filter(
        (f) => f.properties.disease === "Fungal Blight"
      ),
      visible: showFungal,
      filled: true,
      stroked: true,
      getFillColor: [255, 0, 0, 120],
      getLineColor: [200, 0, 0],
      lineWidthMinPixels: 2
    }),

    new GeoJsonLayer({
      id: "leaf-spot",
      data: sampleData.features.filter(
        (f) => f.properties.disease === "Leaf Spot"
      ),
      visible: showLeaf,
      filled: true,
      stroked: true,
      getFillColor: [255, 200, 0, 120],
      getLineColor: [200, 150, 0],
      lineWidthMinPixels: 2
    })
  ];

  return (
    <div>
      <h2>Crop Disease GIS Map</h2>

      <div style={{
        padding: "12px",
        background: "#f1f5f9",
        marginBottom: "10px"
      }}>
        <h3>Map Layer Controls</h3>

        <label>
          <input
            type="checkbox"
            checked={showFungal}
            onChange={() => setShowFungal(!showFungal)}
          />
          🔴 Fungal Blight
        </label>

        <br />

        <label>
          <input
            type="checkbox"
            checked={showLeaf}
            onChange={() => setShowLeaf(!showLeaf)}
          />
          🟡 Leaf Spot
        </label>
      </div>

      <div style={{ height: "450px", width: "100%" }}>
        <DeckGL
          initialViewState={{
            longitude: 83.30,
            latitude: 17.72,
            zoom: 13,
            pitch: 0,
            bearing: 0
          }}
          controller={true}
          layers={layers}
        >
          <Map mapStyle="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json" />
        </DeckGL>
      </div>

      <div style={{
        padding: "12px",
        background: "#f8fafc",
        marginTop: "10px"
      }}>
        <h3>Disease Legend</h3>
        <p>🔴 Red – Fungal Blight</p>
        <p>🟡 Yellow – Leaf Spot</p>
      </div>
    </div>
  );
}

export default MapView;