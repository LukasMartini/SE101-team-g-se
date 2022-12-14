import { ReactMic } from "react-mic";
import { React, useState } from "react";
import "./cards.css";
// credits: sophia

function Popup(props) {
  const [isRecording, setRecording] = useState(false);

  return props.trigger ? (
    <div className="popup">
      <div className="popup-inner">
        <ReactMic
          record={isRecording}
          className="micnone"
          onStop={(blob) => {}}
          onData={(blob) => {
            let fd = new FormData();
            fd.append("blob", blob, "v.webm");
            fetch("http://localhost:8080/mic", {
              method: "POST",
              body: fd,
            });
          }}
        />
        {/* <button onClick={() => setRecording(true)}>start audio</button> */}
        <button className="close-btn" onClick={() => props.setTrigger(false)}>
          x
        </button>
        <iframe
          src={props.children}
          style={{ height: "100%", width: "100%" }}
        />
      </div>
    </div>
  ) : (
    ""
  );
}

function cards({ title, img, feedLink }) {
  const [showOverlay, setOverlay] = useState(false);
  return (
    <>
      <Popup
        trigger={showOverlay}
        setTrigger={setOverlay}
        children={feedLink}
      ></Popup>
      <div className="cardContainer" onClick={() => setOverlay(true)}>
        <h2 style={{ fontWeight: "600" }}> {title} </h2>
        <img
          src="./logo.png"
          style={{
            objectFit: "contain",
            width: "5rem",
            height: "5rem",
            filter: "invert(100%)",
          }}
        />
      </div>
    </>
  );
}

export default cards;
