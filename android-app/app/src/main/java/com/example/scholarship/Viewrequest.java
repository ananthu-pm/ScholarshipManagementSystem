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

public class Viewrequest extends AppCompatActivity  implements JsonResponse {

    ListView l1;
    SharedPreferences sh;
    String[] date,statu,rejectnotification,images,value,notification_id,crid,cids;
    public static String cid,cou,stat;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewrequest);

        l1=(ListView) findViewById(R.id.list);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) Viewrequest.this;
        String q = "/Viewrequest?log_id=" +sh.getString("login_id", "");
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


                date = new String[ja1.length()];
                statu = new String[ja1.length()];
                rejectnotification = new String[ja1.length()];

                images = new String[ja1.length()];
                notification_id= new String[ja1.length()];
                crid= new String[ja1.length()];
                cids=new String[ja1.length()];



                value = new String[ja1.length()];


                for (int i = 0; i < ja1.length(); i++) {
                    date[i] = ja1.getJSONObject(i).getString("rdate");
                    statu[i] = ja1.getJSONObject(i).getString("rstatus");


                    images[i] = ja1.getJSONObject(i).getString("scholarship");
                    crid[i] = ja1.getJSONObject(i).getString("request_id");
                    cids[i]=ja1.getJSONObject(i).getString("scholarship_id");








                    value[i] = "date:" + date[i] + "\n status: " + statu[i] + "\n scholarship: " + images[i]   ;

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), R.layout.custtext, value);

                l1.setAdapter(ar);



            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), "no request", Toast.LENGTH_LONG).show();

        }
    }
}