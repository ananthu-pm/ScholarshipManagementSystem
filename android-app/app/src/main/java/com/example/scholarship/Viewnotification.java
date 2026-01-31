package com.example.scholarship;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Viewnotification extends AppCompatActivity implements JsonResponse {

    ListView l1;
    SharedPreferences sh;
    String[] classes,fees,date,statu,class_id,value;
    public static String cid,rid,stat;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewnotification);

        l1=(ListView) findViewById(R.id.list);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


        JsonReq JR = new JsonReq();
        JR.json_response = (com.example.scholarship.JsonResponse) Viewnotification.this;
        String q = "/Viewnotification?log_id=" +sh.getString("login_id", "");
        q = q.replace(" ", "%20");
        JR.execute(q);
    }

    @Override
    public void response(JSONObject jo) {
        try {

            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");


                classes = new String[ja1.length()];

                class_id = new String[ja1.length()];

                value = new String[ja1.length()];


                for (int i = 0; i < ja1.length(); i++) {
                    classes[i] = ja1.getJSONObject(i).getString("notification");
                    class_id[i] = ja1.getJSONObject(i).getString("notification_id");







                    value[i] = "notification:" + classes[i]    ;

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), R.layout.custtext, value);

                l1.setAdapter(ar);

            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), "no notification", Toast.LENGTH_LONG).show();

        }
    }
}