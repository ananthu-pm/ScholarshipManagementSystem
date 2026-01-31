package com.example.scholarship;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class viewscholarship extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {


    ListView l1;
    SharedPreferences sh;
    String[] date,statu,rejectnotification,images,value,notification_id,crid,cids,schid;
    public static String cuid,cou,stat;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewscholarship);

        l1=(ListView) findViewById(R.id.list);
        l1.setOnItemClickListener(this);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) viewscholarship.this;
        String q = "/viewscholarship?log_id=" +sh.getString("login_id", "");
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
                schid=new String[ja1.length()];


                value = new String[ja1.length()];


                for (int i = 0; i < ja1.length(); i++) {
                    date[i] = ja1.getJSONObject(i).getString("date");
                    statu[i] = ja1.getJSONObject(i).getString("status");

                    rejectnotification[i] = ja1.getJSONObject(i).getString("scholarship");
                    images[i] = ja1.getJSONObject(i).getString("category");
                    crid[i] = ja1.getJSONObject(i).getString("startdate");
                    cids[i]=ja1.getJSONObject(i).getString("enddate");
                    schid[i] = ja1.getJSONObject(i).getString("scholarship_id");







                    value[i] = " scholarship: " + rejectnotification[i]+ "\n category: " + images[i]+  "\nstartdate:" + crid[i]+  "\nenddate:" + cids[i]+  "\ndate:" + date[i] + "\n status: " + statu[i]   ;

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), R.layout.custtext, value);

                l1.setAdapter(ar);



            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), "no scholarship", Toast.LENGTH_LONG).show();

        }
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        cuid=schid[i];

        final CharSequence[] items = {"Send Request"};

        AlertDialog.Builder builder = new AlertDialog.Builder(viewscholarship.this);
        builder.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {
                if (items[item].equals("Send Request")) {

                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) viewscholarship.this;
                    String q = "/sendrequest?log_id=" +sh.getString("login_id", "")+"&sid="+cuid;
                    q = q.replace(" ", "%20");
                    JR.execute(q);


                }


            }

        });
        builder.show();
    }
    }
