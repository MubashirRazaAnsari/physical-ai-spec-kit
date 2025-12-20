import urllib.request
import urllib.error
import json
import ssl

# Credentials provided
QDRANT_URL = "https://bae94f35-1cf2-4a9a-9013-49c56d993bb7.europe-west3-0.gcp.cloud.qdrant.io"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.ZGCkfJUN0SR4jVe6lxXqqCmWIqjSRvU1ZbV5YNby3Ac"
COLLECTION_NAME = "physical_ai_book"
GOOGLE_API_KEY = "AIzaSyAMVT4w3p9I1PH0_erEzIKm4ludKi9pzz0"

def test_qdrant():
    print("\n1. Testing Qdrant Connection (Standard Lib)...")
    url = f"{QDRANT_URL}/collections/{COLLECTION_NAME}"
    headers = {
        "api-key": QDRANT_API_KEY,
        "Content-Type": "application/json"
    }
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.load(response)
            status = data.get("status")
            if status == "ok":
                vectors_count = data.get("result", {}).get("vectors_count", "Unknown")
                print(f"✅ Connected to Qdrant successfully.")
                print(f"   Collection '{COLLECTION_NAME}' exists.")
                print(f"   Vector Count: {vectors_count}")
                return True
            else:
                print(f"⚠️ Qdrant returned unexpected status: {status}")
                return False
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"❌ Connected, but Collection '{COLLECTION_NAME}' was NOT FOUND.")
        elif e.code == 401 or e.code == 403:
             print(f"❌ Authorization Failed. Check QDRANT_API_KEY.")
        else:
            print(f"❌ HTTP Error: {e.code} {e.reason}")
        return False
    except Exception as e:
        print(f"❌ Connection Failed: {str(e)}")
        return False

def test_google():
    print("\n2. Testing Google Gemini Connection (Standard Lib)...")
    # Using gemini-1.5-flash as it is usually available and free tier
    model = "gemini-1.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GOOGLE_API_KEY}"
    
    payload = {
        "contents": [{
            "parts": [{"text": "Say 'OK'"}]
        }]
    }
    data = json.dumps(payload).encode('utf-8')
    
    headers = {"Content-Type": "application/json"}
    
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.load(response)
            # Check if we got a candidate
            try:
                text = result['candidates'][0]['content']['parts'][0]['text']
                print(f"✅ Connected to Google Gemini successfully.")
                print(f"   Model Response: {text.strip()}")
                return True
            except (KeyError, IndexError):
                print(f"⚠️ Connected, but response format was unexpected: {json.dumps(result)[:100]}...")
                return True # Still connected effectively
                
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error: {e.code} {e.reason}")
        if e.code == 400:
             print("   (Bad Request - API Key might be invalid or model not supported)")
        if e.code == 404:
             print("   (Not Found - The model name 'gemini-1.5-flash' might be wrong or you don't have access to it)")
        return False
    except Exception as e:
        print(f"❌ Connection Failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("--- DIAGNOSTIC REPORT (No Dependencies) ---")
    q_ok = test_qdrant()
    g_ok = test_google()
    
    if q_ok and g_ok:
        print("\n✅✅ SUCCESS: Both backend services are accessible with provided credentials.")
    else:
        print("\n❌❌ FAILURE: One or more services are not working correctly.")
