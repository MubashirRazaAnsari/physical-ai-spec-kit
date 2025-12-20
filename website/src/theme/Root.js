import React from 'react';
import FloatingChatWidget from '../components/FloatingChatWidget/FloatingChatWidget';

// Root component that wraps the entire app
export default function Root({ children }) {
  return (
    <>
      {children}
      <FloatingChatWidget />
    </>
  );
}